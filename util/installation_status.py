import os
from util.dependency_check import check_git,check_python
from util.util import is_folder_exist_check
from util.json_tools_projects import get_pref_project_data
# import requests

def pref_project_path(project):
    project_id = project['id']
    if get_pref_project_data(project_id):
        pref_project_data =get_pref_project_data(project_id)
        project_pref_path = pref_project_data['path']
        project_pref_isSet = pref_project_data['isSet']
        if project_pref_isSet:
            return os.path.abspath(project_pref_path)
        else:
            return os.path.abspath(project['repo_name'])
    else:
        return os.path.abspath(project['repo_name'])
        
def check_project(project):
    project_path = pref_project_path(project)
    if project['type'] == "app":
        if project_path and is_folder_exist_check(project_path):
            return True
        else:
            return False
    elif project['type'] == "webui_extension":
        if is_folder_exist_check(f"{project['webui_path']}\extensions\{project['repo_name']}"):
            return True
        else:
            return False

def check_project_venv(project):
    project_path = pref_project_path(project)
    if project['type'] == "app":
        if project_path and is_folder_exist_check(project_path):
            if is_folder_exist_check(os.path.join(project_path, 'venv')):
                return True
            else:
                return False
        else:
            return False             

def get_last_commit_hash_local(app_info):
    if check_git():
        import git
        if app_info['type'] == "app":
            repo_path = pref_project_path(app_info)
        elif app_info['type'] == "webui_extension":
            repo_path = os.path.join(app_info['webui_path'], 'extensions', app_info['repo_name'])
        else:
            print("Error: Invalid app type")
            return None
        if not os.path.exists(repo_path):
            return None
        try:
            repo = git.Repo(repo_path)
            last_commit_hash = repo.head.object.hexsha
            return last_commit_hash
        except git.InvalidGitRepositoryError:
            return None
        except ValueError:
            return None  

def check_git_python():
    if check_python() and check_git():
        return True  
    else:
        return False            
def get_last_commit_hash_remote(github_url):
    # extract the owner and repo name from the GitHub URL
    # url_parts = github_url.split('/')
    # owner = url_parts[-2]
    # repo_name = url_parts[-1].split('.')[0]

    # # construct the API endpoint URL
    # api_url = f"https://api.github.com/repos/{owner}/{repo_name}/commits"

    # try:
    #     # make a GET request to the API endpoint
    #     response = requests.get(api_url)

    #     # extract the last commit hash from the response
    #     last_commit_hash = response.json()[0]['sha']

    #     # return the last commit hash
    #     return last_commit_hash
    # except requests.exceptions.RequestException as e:
    #     print(f"Error: {e}")
    #     return None
    pass        
