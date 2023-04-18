import subprocess
import os
from util.CONSTANTS import *
import requests
import util.installation_status as installation_status
from util.json_tools_projects import get_pref_project_data

def convert_to_backslashes(file_path):
    return file_path.replace("/", "\\")

def get_project_path(project_data):
    if pref_project_path(project_data):
        return convert_to_backslashes(pref_project_path(project_data))
    else:
        return os.path.abspath(project_data['repo_name'])

def get_venv_path(project_data):
    return f"{os.path.join(get_project_path(project_data), 'venv')}"

def get_entry_point(project_data, key):
    return os.path.join(get_project_path(project_data), project_data['entry_point'][key])

def get_pref_project_path(project_name, project_pref_path):
    project_path = os.path.join(project_pref_path,project_name)
    return project_path

def pref_project_path(project_data):
    project_id = project_data['id']
    if get_pref_project_data(project_id):
        pref_project_data =get_pref_project_data(project_id)
        if pref_project_data['isSet']:
            return pref_project_data['path']
        else:
            return False

def clone_repo(project_data):
    project_name = project_data['repo_name']
    git_clone_url = project_data['git_clone_url']
    project_path = get_project_path(project_data)
    subprocess.run(["git", "clone", git_clone_url, project_path]) 
    print(f"{project_name} cloned into {project_path}")

def create_virtual_environment(project_data, args=[]):
    project_name = project_data['repo_name']
    project_path = get_project_path(project_data)
    venv_path = get_venv_path(project_data)
    print(f"Creating virtual environment for {project_name} at {venv_path} ")
    subprocess.run(["python", "-m", "venv", venv_path], shell=True)         
    print(f"Virtual environment created for {project_name} at {venv_path}")

def update(project_data,args=[]):
    project_path = get_project_path(project_data)
    print(f"Updating {project_data['repo_name']} at {project_path}")
    subprocess.run(["git", "pull"], cwd=project_path)

def uninstall(project_data,args=[]):
    project_path = get_project_path(project_data)
    print(f"Uninstalling {project_data['repo_name']} deleting {project_path} folder.")
    subprocess.run(["rd", "/s", "/q", project_path], shell=True)
    print(f"{project_data['repo_name']} uninstalled {project_path} folder deleted.")

def launch(project_data, args=[]):
    project_path = get_project_path(project_data)
    venv_path = get_venv_path(project_data)
    launch_path = get_entry_point(project_data, 'launch')
    print(f"launching {project_data['repo_name']}")
    installation_status_venv = installation_status.check_project_venv(project_data)
    installation_status_project = installation_status.check_project(project_data)

    if not installation_status_venv:
        print(f"Virtual environment (venv) not found for {project_data['repo_name']} at {project_path}. Will create a new one.")
        install(project_data,args=[])

    if installation_status_project:
        # print(f"{project_data['repo_name']} venv installed")
        command_len = len(launch_path.split())
        cmd_launch = project_data['entry_point']['launch']
        activate_script = f"{venv_path}/Scripts/activate.bat"
        cmd_command = f'cmd /K "{activate_script} && {cmd_launch} {" ".join(args)}"'
        if launch_path.endswith(".py") and command_len == 1:
            subprocess.run([f"{venv_path}/Scripts/python", launch_path, *args], cwd=project_path)
        elif launch_path.endswith(".py") and command_len > 1:
            subprocess.run(cmd_command, cwd=project_path, shell=True)           
        elif launch_path.endswith(".bat"):
            subprocess.run([launch_path, *args], cwd=project_path)
        else:
            subprocess.run(cmd_command, cwd=project_path, shell=True)      
    else:
        print(f"Failed to launch {project_data['repo_name']} venv not installed.")
        
def install(project_data,args=[]):
    project_path = get_project_path(project_data) 
    print(f"installing {project_data['repo_name']} with at {project_path}")
    clone_repo(project_data)
    create_virtual_environment(project_data)
    venv_path = get_venv_path(project_data)
    install_path = get_entry_point(project_data, 'install') 
    # print("venv_path",f"{venv_path}/Scripts/python")

    command_len = len(install_path.split())
    cmd_launch = project_data['entry_point']['launch']
    activate_script = f"{venv_path}/Scripts/activate.bat"
    cmd_command = f'cmd /K "{activate_script} && {cmd_launch} {" ".join(args)}"'

    if project_data['install_requirements']:
        install_requirements(project_data)
    if project_data['install_instructions_available']:
        install_instructions(project_data)    
    if install_path.endswith(".py") and command_len == 1:
        subprocess.run([f"{venv_path}/Scripts/python", install_path, *args], cwd=project_path)
    elif install_path.endswith(".py") and command_len > 1:
        subprocess.run(cmd_command, cwd=project_path, shell=True)         
    elif install_path.endswith(".bat"):
        subprocess.run([install_path, *args], cwd=project_path)
    else:
        subprocess.run(cmd_command, cwd=project_path, shell=True)         

def delete_virtual_environment(project_data,args=[]):
    venv_path = get_venv_path(project_data)
    print(f"Deleting virtual environment for {project_data['repo_name']} at {venv_path}")
    subprocess.run(["rd", "/s", "/q", venv_path], shell=True)
    print(f"virtual environment deleted for {project_data['repo_name']}")
    
def install_cuda(project_data):
    project_path = get_project_path(project_data)
    venv_path = get_venv_path(project_data)
    print(f"installing cuda")
    cmd = f"{venv_path}/Scripts/python -m pip install torch==1.13.1 torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117 xformers"
    subprocess.run(cmd, shell=True, cwd=project_path)
    print(f"cuda installed")

def install_requirements(project_data):
    project_path = get_project_path(project_data)
    venv_path = get_venv_path(project_data)
    print(f"Installing requirements for {project_data['repo_name']} at {venv_path}")
    if project_data['install_cuda']:
        install_cuda(project_data)
    subprocess.run([f"{venv_path}/Scripts/python","-m", "pip","install","-r","requirements.txt"], cwd=project_path)
    print(f"{project_data['repo_name']} requirements installed at {venv_path}")

def install_instructions(project_data):
    project_path = get_project_path(project_data)
    venv_path = get_venv_path(project_data)
    print(f"installing requirements for {project_data['repo_name']}")

    for command in project_data["install_instructions"]:
        subprocess.run([f"{venv_path}/Scripts/python"] + command.split(), cwd=project_path)
        # print([f"{venv_path}/Scripts/python"] + command.split(), cwd=project_path)
        print(f"{project_data['repo_name']} requirements installed")

def install_webui_extension(project_data,args=[]):
    print(f"installing {project_data['repo_name']}")
    subprocess.run(["git","clone",project_data["git_clone_url"],f"{project_data['webui_path']}\extensions\{project_data['repo_name']}"]) 
    print(f"{project_data['repo_name']} installed")

def update_webui_extension(project_data,args=[]):
    print(f"updating {project_data['repo_name']}")
    subprocess.run(["git","pull"], cwd=f"{project_data['webui_path']}\extensions\{project_data['repo_name']}")

def uninstall_webui_extension(project_data,args=[]):
    print(f"uninstalling {project_data['repo_name']}")
    subprocess.run(["rd", "/s", "/q", f"{project_data['webui_path']}\extensions\{project_data['repo_name']}"], shell=True)
    print(f"{project_data['repo_name']} uninstalled")

def download_models(project_data, skip_existing=True):
    base_url = "https://huggingface.co/datasets/disty/seait_ControlNet-modules-safetensors/resolve/main/"
    download_folder = os.path.join(project_data['webui_path'], 'models', 'ControlNet')
    os.makedirs(download_folder, exist_ok=True)

    for model in CN_MODELS:
        file_path = os.path.join(download_folder, model)
        
        if skip_existing and os.path.exists(file_path):
            print(f"{model} already exists. Skipping download.")
            continue

        url = base_url + model
        response = requests.get(url)

        if response.status_code == 200:
            model_size_mb = int(response.headers.get("Content-Length", 0)) / (1024 * 1024)
            print(f"Downloading {model} ({model_size_mb:.2f} MB)")
            with open(file_path, "wb") as f:
                f.write(response.content)
            print(f"{model} downloaded.")
        else:
            print(f"Error: Failed to download {model}. Status code: {response.status_code}")

    print("All models downloaded.")

def download_comfyui_models(project_data):
    if project_data["id"] == 2:
        # print(f"downloading models for {project_data['repo_name']}")
        project_path = get_project_path(project_data) 
        checkpoints_path = os.path.join(f"{project_path}/{project_data['checkpoints_path']}")
        # subprocess.run(["git","clone",project_data["models_path"],f"{project_data['webui_path']}\models\ControlNet"]) 
        # download_file(project_data["download_models_path"], project_data['checkpoints_path']) 
        # print(checkpoints_path) 
        # download_file(project_data['download_models_path'],f"C:/repos/seai/ComfyUI/models/checkpoints/{project_data['download_models_path']}")     
        print(f"{project_data['repo_name']} models downloaded")    

methods = {
    "clone": clone_repo,
    "update": update,
    "delete_venv": delete_virtual_environment,
    "create_venv": create_virtual_environment,
    "uninstall": uninstall,
    "launch": launch,
    "install": install,
    "install_webui_extension": install_webui_extension,
    "uninstall_webui_extension": uninstall_webui_extension,
    "update_webui_extension": update_webui_extension,
    "download_models": download_models,
}
