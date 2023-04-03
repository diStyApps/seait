import subprocess
import os
from util.CONSTANTS import *
import requests
def get_project_path(app_info):
    return os.path.abspath(app_info['repo_name'])

def get_venv_path(app_info):
    return os.path.join(get_project_path(app_info), 'venv')

def get_entry_point(app_info, key):
    return os.path.join(get_project_path(app_info), app_info['entry_point'][key])

pre_installed_python_path = os.path.abspath(PRE_INSTALLED_PYTHON_PATH)
usePreInstalledPython = False

def clone_repo(app_info):
    project_path = get_project_path(app_info)
    print(f"cloning {app_info['repo_name']}")
    subprocess.run(["git", "clone", app_info["git_clone_url"], project_path]) 
    # print(f"{app_info['repo_name']} cloned")

def update(app_info):
    project_path = get_project_path(app_info)
    print(f"updating {app_info['repo_name']}")
    subprocess.run(["git", "pull"], cwd=project_path)

def uninstall(app_info):
    project_path = get_project_path(app_info)
    print(f"Uninstalling {app_info['repo_name']}")
    subprocess.run(["rd", "/s", "/q", project_path], shell=True)
    print(f"{app_info['repo_name']} uninstalled")

# def launch(app_info,args):
#     project_path = get_project_path(app_info)
#     venv_path = get_venv_path(app_info)
#     launch_path = get_entry_point(app_info, 'launch')
#     print(f"launching {app_info['repo_name']}")
#     subprocess.run([f"{venv_path}/Scripts/python", launch_path,*args], cwd=project_path)

def launch(app_info, args):
    # print(app_info)
    project_path = get_project_path(app_info)
    venv_path = get_venv_path(app_info)
    launch_path = get_entry_point(app_info, 'launch')
    print(f"launching {app_info['repo_name']}")
    
    if launch_path.endswith(".py"):
        subprocess.run([f"{venv_path}/Scripts/python", launch_path, *args], cwd=project_path)
    elif launch_path.endswith(".bat"):
        subprocess.run([launch_path, *args], cwd=project_path)
    else:
        raise ValueError("Unsupported file format for launch_path")    

def install(app_info,args):
    print(f"installing {app_info['repo_name']}")
    clone_repo(app_info)
    create_virtual_environment(app_info)
    project_path = get_project_path(app_info) 
    venv_path = get_venv_path(app_info)
    install_path = get_entry_point(app_info, 'install') 
    print("venv_path",f"{venv_path}/Scripts/python")

    if app_info['install_requirements']:
        install_requirements(app_info)
    # if app_info['id'] == 2:
    #     download_comfyui_models(app_info)
    # subprocess.run([f"{venv_path}/Scripts/python", install_path,*args], cwd=project_path)
    if install_path.endswith(".py"):
        subprocess.run([f"{venv_path}/Scripts/python", install_path, *args], cwd=project_path)
    elif install_path.endswith(".bat"):
        subprocess.run([install_path, *args], cwd=project_path)
    else:
        raise ValueError("Unsupported file format for launch_path")       

def delete_virtual_environment(app_info,args=[]):
    venv_path = get_venv_path(app_info)
    print(f"Deleting virtual environment for {app_info['repo_name']}")
    subprocess.run(["rd", "/s", "/q", venv_path], shell=True)
    print(f"virtual environment deleted for {app_info['repo_name']}")

def create_virtual_environment(app_info):
    venv_path = get_venv_path(app_info)
    print(f"creating virtual environment for {app_info['repo_name']}")
    if usePreInstalledPython:
        subprocess.run([pre_installed_python_path, "-m", "venv", venv_path], shell=True)     
    else:
        subprocess.run(["python", "-m", "venv", venv_path], shell=True) 
    print(f"virtual environment created for {app_info['repo_name']}")

def install_cuda(app_info):
    project_path = get_project_path(app_info)
    venv_path = get_venv_path(app_info)
    print(f"installing cuda")
    cmd = f"{venv_path}/Scripts/python -m pip install torch==1.13.1 torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu117 xformers"
    subprocess.run(cmd, shell=True, cwd=project_path)
    print(f"cuda installed")

def install_requirements(app_info):
    project_path = get_project_path(app_info)
    venv_path = get_venv_path(app_info)
    print(f"installing requirements {app_info['repo_name']}")
    if app_info['install_cuda']:
        install_cuda(app_info)
    subprocess.run([f"{venv_path}/Scripts/python","-m", "pip","install","-r","requirements.txt"], cwd=project_path)
    print(f"{app_info['repo_name']} requirements installed")

def install_webui_extension(app_info):
    print(f"installing {app_info['repo_name']}")
    # venv_path = os.path.abspath(f"{app_info['webui_path']}venv")
    # project_path = f"{app_info['webui_path']}\extensions\{app_info['repo_name']}"
    # print(f"{app_info['webui_path']}\extensions\{app_info['repo_name']}")

    subprocess.run(["git","clone",app_info["git_clone_url"],f"{app_info['webui_path']}\extensions\{app_info['repo_name']}"]) 
    # subprocess.run([f"C:/repos/seait/stable-diffusion-webui/venv/Scripts/python","-m", "pip","install","-r","requirements.txt"], cwd=project_path)
    # print(os.path.abspath(f"{app_info['webui_path']}\extensions\{app_info['repo_name']}"))
    # print(os.path.abspath(f"{app_info['webui_path']}venv/Scripts/python"))

    # C:\repos\seait\stable-diffusion-webui\venv/Scripts/python
    print(f"{app_info['repo_name']} installed")

def update_webui_extension(app_info):
    print(f"updating {app_info['repo_name']}")
    subprocess.run(["git","pull"], cwd=f"{app_info['webui_path']}\extensions\{app_info['repo_name']}")

def uninstall_webui_extension(app_info):
    print(f"uninstalling {app_info['repo_name']}")
    subprocess.run(["rd", "/s", "/q", f"{app_info['webui_path']}\extensions\{app_info['repo_name']}"], shell=True)
    print(f"{app_info['repo_name']} uninstalled")

def download_models(app_info, skip_existing=True):
    base_url = "https://huggingface.co/datasets/disty/seait_ControlNet-modules-safetensors/resolve/main/"
    download_folder = os.path.join(app_info['webui_path'], 'models', 'ControlNet')
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

def download_comfyui_models(app_info):
    if app_info["id"] == 2:
        # print(f"downloading models for {app_info['repo_name']}")
        project_path = get_project_path(app_info) 
        checkpoints_path = os.path.join(f"{project_path}/{app_info['checkpoints_path']}")
        # subprocess.run(["git","clone",app_info["models_path"],f"{app_info['webui_path']}\models\ControlNet"]) 
        # download_file(app_info["download_models_path"], app_info['checkpoints_path']) 
        # print(checkpoints_path) 
        # download_file(app_info['download_models_path'],f"C:/repos/seai/ComfyUI/models/checkpoints/{app_info['download_models_path']}")     
        print(f"{app_info['repo_name']} models downloaded")    

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
