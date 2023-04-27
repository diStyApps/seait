import os
import shutil
import tempfile
from datetime import datetime
import datetime

def rollback(src, dst, moved_items, temp_dir, log):
    print("Rolling back changes...")
    rollback_date = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    dst_folder_name = os.path.basename(dst)
    rollbacks_folder = os.path.join(os.path.dirname(src), 'rollbacks')
    os.makedirs(rollbacks_folder, exist_ok=True)
    rollback_folder = os.path.join(rollbacks_folder, f"rollback_{rollback_date}-{dst_folder_name}")
    os.makedirs(rollback_folder)

    for item in moved_items:
        src_item_path = os.path.join(src, item)
        temp_item_path = os.path.join(temp_dir, item)

        try:
            if os.path.exists(src_item_path):
                shutil.move(src_item_path, os.path.join(rollback_folder, item))
            shutil.move(temp_item_path, src_item_path)
        except Exception as e:
            print(f"Error rolling back item {item}: {e}")

    log_file = os.path.join(rollback_folder, "rollback_log.txt")
    with open(log_file, "w") as f:
        f.write(f"Source: {src}\n")
        f.write(f"Destination: {dst}\n")
        f.write("\nError:\n")
        f.write(f"  {log}\n")
        f.write("\nList of moved files:\n")
        for item in moved_items:
            f.write(f"  {item}\n")

    print(f"Files moved to rollback folder: {rollback_folder}")

def create_symlink_internal(src, dst, verbose=False, use_rollback=True):
    moved_items = []
    temp_dir = tempfile.mkdtemp()

    try:
        if os.path.exists(dst) and os.path.isdir(dst):
            for item in os.listdir(dst):
                src_item_path = os.path.join(src, item)
                dst_item_path = os.path.join(dst, item)

                if not os.path.exists(src_item_path):
                    if verbose:
                        print(f"Moving {dst_item_path} to {src_item_path}")

                    shutil.move(dst_item_path, src_item_path)
                    moved_items.append(item)

            os.rmdir(dst)
        os.symlink(src, dst, target_is_directory=True)
        print("Symbolic link created successfully")

        shutil.rmtree(temp_dir)

    except Exception as e:
        print(f"Error creating symlink: {e}")
        if use_rollback:
            rollback(src, dst, moved_items, temp_dir, str(e))
        shutil.rmtree(temp_dir)
        raise

def create_symlink(src, dst, verbose=False, use_rollback=True):
    try:
        create_symlink_internal(src, dst, verbose=verbose, use_rollback=use_rollback)
    except Exception as e:
        print(f"Failed to create symlink: {e}")

def remove_symlink(symlink_path, create_folder=False):
    if os.path.islink(symlink_path):
        os.unlink(symlink_path)
        print(f"Symbolic link removed: {symlink_path}")
        
        if create_folder:
            os.makedirs(symlink_path)
            print(f"New folder created: {symlink_path}")
    else:
        print(f"The path is not a symbolic link: {symlink_path}")
