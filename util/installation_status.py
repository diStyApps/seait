import os
import util.dependency_check as depcheck
# import requests


def is_file_exist_check(file_path):
    if os.path.isfile(file_path):
        # print('isfile_exist_check:',file_path, ' FILE EXIST')
        return True
    if not os.path.isfile(file_path):
        # print('isfile_exist_check:',file_path,' FILE NOT EXIST')    
        return False   
    
def is_folder_exist_check(file_path):
    if os.path.exists(file_path):
        # print('isfolder_exist_check:',file_path, ' FOLDER EXIST')
        return True
    if not os.path.exists(file_path):
        # print('isfolder_exist_check:',file_path,' FOLDER NOT EXIST')    
        return False   

def check_project(project):
    project_path = os.path.abspath(project['repo_name'])
    if project['type'] == "app":
        if is_folder_exist_check(project_path):
            # print(f"{project['repo_name']} project installed")      
            if is_folder_exist_check(os.path.join(project_path, 'venv')):
                # print(f"{project['repo_name']} venv installed")
                return True
            else:
                # print(f"{project['repo_name']} venv not installed")
                return False
        else:
            # print(f"{project['repo_name']} project not installed")
            return False
    elif project['type'] == "webui_extension":
        if is_folder_exist_check(f"{project['webui_path']}\extensions\{project['repo_name']}"):
            # print(f"extension {project['repo_name']} is installed")
            return True
        else:
            # print(f"extension {project['repo_name']} is not installed")
            return False

def check_git_python():
    if depcheck.check_python() and depcheck.check_git():
        # print("Python and git installed")
        return True  
    else:
        # print("Python or git not installed")
        return False               

def get_last_commit_hash_local(app_info):
    if depcheck.check_git():
        import git
        if app_info['type'] == "app":
            repo_path = app_info['repo_name']
        elif app_info['type'] == "webui_extension":
            repo_path = os.path.join(app_info['webui_path'], 'extensions', app_info['repo_name'])
        else:
            print("Error: Invalid app type")
            return None
        
        if not os.path.exists(repo_path):
            # print(f"Error: Path {repo_path} does not exist")
            return None
        
        try:
            # open the repository at the specified path
            repo = git.Repo(repo_path)

            # get the last commit hash
            last_commit_hash = repo.head.object.hexsha

            # return the last commit hash
            return last_commit_hash
        except git.InvalidGitRepositoryError:
            # print(f"Error: Invalid git repository at {repo_path}")
            return None
        except ValueError:
            # print(f"Error: Invalid value")
            return None  
          
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
