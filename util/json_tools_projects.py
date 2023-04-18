import json
import os
file_path = "projects_preferences.json"

def load_project_preferences(file_path):
    if not os.path.exists(file_path):
        default_project_preferences = {
            "set_project_paths": [
                {
                    "projects": []
                }
            ]
        }
        with open(file_path, "w") as file:
            json.dump(default_project_preferences, file, indent=4)
    
    with open(file_path, "r") as file:
        return json.load(file)

def save_project_preferences(project_preferences, file_path):
    with open(file_path, "w") as file:
        json.dump(project_preferences, file, indent=4)

def add_project(project_id, path, isSet):
    project_preferences = load_project_preferences(file_path)
    projects = project_preferences["set_project_paths"][0]["projects"]

    existing_project = None
    for project in projects:
        if project["project_id"] == project_id:
            existing_project = project
            break

    if existing_project:
        existing_project["path"] = path
        existing_project["isSet"] = isSet
    else:
        new_project = {"project_id": project_id, "path": path, "isSet": isSet}
        projects.append(new_project)

    save_project_preferences(project_preferences, file_path)

def update_project(project_id, path, isSet, file_path):
    project_preferences = load_project_preferences(file_path)
    projects = project_preferences["set_project_paths"][0]["projects"]

    for project in projects:
        if project["project_id"] == project_id:
            if path is not None:
                project["path"] = path
            if isSet is not None:
                project["isSet"] = isSet
            break

    save_project_preferences(project_preferences, file_path)

def delete_project(project_id, file_path):
    project_preferences = load_project_preferences(file_path)
    projects = project_preferences["set_project_paths"][0]["projects"]

    for project in projects:
        if project["project_id"] == project_id:
            projects.remove(project)
            break

    save_project_preferences(project_preferences, file_path)

def get_pref_project_data(project_id):
    project_preferences = load_project_preferences(file_path)
    projects = project_preferences["set_project_paths"][0]["projects"]

    for project in projects:
        if project["project_id"] == project_id:
            return project

    return None

def set_project_active(project_id, isSet):
    project_preferences = load_project_preferences(file_path)
    projects = project_preferences["set_project_paths"][0]["projects"]

    for project in projects:
        if project["project_id"] == project_id:
            project["isSet"] = isSet
            break

    save_project_preferences(project_preferences, file_path)

# add_project(1, "C:\\repos\\-SEAIT",False) 

