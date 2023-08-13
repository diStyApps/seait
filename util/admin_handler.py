import sys
import os
import ctypes

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def run_as_admin():
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
    sys.exit(0)  # Exit the current non-admin process


if is_admin():
    print("Running with administrator privileges.")
else:
    print("Running without administrator privileges.")

    # admin_dialog_layout = [
    #     [sg.Text('Do you want to run this program as an administrator?')],
    #     [sg.Button('Yes'), sg.Button('No')]
    # ]

    # admin_dialog_window = sg.Window('Administrator Privileges', admin_dialog_layout)

    # while True:
    #     admin_dialog_event, admin_dialog_values = admin_dialog_window.read()

    #     if admin_dialog_event == sg.WIN_CLOSED or admin_dialog_event == 'No':
    #         admin_dialog_window.close()
    #         break

    #     if admin_dialog_event == 'Yes':
    #         if not is_admin():
    #             run_as_admin()
    #         admin_dialog_window.close()
    #         break

if __name__ == '__main__':
    sg.theme('Dark Gray 15')

    sg.set_options(
        # button_color=('white', 'green'),
        # button_color=(color.LIGHT_GRAY, color.GRAY),
        # element_size=(50, 20),
        # auto_size_buttons=True,
        # font=('Helvetica', 14),
        # background_color='lightgray',
        # text_color='black',
        # ttk_theme='classic',
        sbar_width=15,sbar_trough_color=0,sbar_arrow_width=8,    
        suppress_raise_key_errors=True,
        suppress_error_popups=True,
        suppress_key_guessing=True    
    )

    def suppress_errors(*args, **kwargs):
        pass

    sg.Print = suppress_errors  

    def reopen_window(window):
        window.close()
        main()  

    # if not is_admin():
    #     run_as_admin()
    is_admin()
    main()

# Get the user's Documents folder
documents_folder = os.path.expanduser('~\\Documents')

# Define your app's folder and downloaded content folder
app_folder = 'Seait'
downloaded_content_folder = 'DownloadedContent'

# Construct the full path
full_path = os.path.join(documents_folder, app_folder, downloaded_content_folder)
os.makedirs(full_path, exist_ok=True)
print(full_path)


def get_system_home_folder_path():
    return os.path.expanduser('~').replace("\\",'/')

def get_folder_with_system_home_folder_path(folder,slash=True):
    if slash:
        return f'{get_system_home_folder_path()}/{folder}'      
    else:
        return f'{get_system_home_folder_path()}{folder}'      

def load_input_folders_info(file_name_on_load):
    system_home_folder_path = os.path.expanduser('~')
    system_home_folder_path_replaced_slashes = system_home_folder_path.replace("\\",'/')
    system_home_folder_path = f'{system_home_folder_path_replaced_slashes}/'

    