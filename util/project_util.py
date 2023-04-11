
import re
from util.CONSTANTS import *

def update_project_args(project_id, arg_name):
    if project_id not in project_args:
        project_args[project_id] = []

    if arg_name in project_args[project_id]:
        project_args[project_id].remove(arg_name)
    else:
        project_args[project_id].append(arg_name)

def update_project_args_from_string(project_id, values_string):
    args_list = values_string.split()
    for arg_name in args_list:
        if arg_name not in project_args.get(project_id, []):
            update_project_args(project_id, arg_name)

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