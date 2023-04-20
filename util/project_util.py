import re
from util.CONSTANTS import *

def get_project_by_id(projects, project_id):
    for project in projects:
        if project.get("id") == project_id:
            return project
    return None

def get_project_id(event):
    return int(re.search(r"_\d+", event).group(0)[1:])

def get_function_and_project_id(event):
    id_number = get_project_id(event)
    method = re.search(r"-selected_app_func_\d+_(.+)_btn-", event).group(1)
    return id_number,method