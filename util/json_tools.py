import json
PREFERENCES_FILE_NAME = 'preferences.json'

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def save_json_file(filename_path,dictionary,add_default_ext=False):
    if add_default_ext:
        with open(f'{filename_path}.json', 'w') as fp:
            json.dump(dictionary, fp,  indent=4,cls=SetEncoder)
    else:
        with open(filename_path, 'w') as fp:
            json.dump(dictionary, fp,  indent=4,cls=SetEncoder)
            
    return read_json_file(filename_path)

def read_json_file(filename_path,add_default_ext=False):
    if add_default_ext:
        with open(f'{filename_path}.json', 'r') as f:
            x = json.load(f) # x is a python dictionary in this case
        return x
    else:
        with open(filename_path, 'r') as f:
            x = json.load(f) # x is a python dictionary in this case
        return x

def read_json_file_full_path(filename_path):
    with open(filename_path, 'r') as f:
        x = json.load(f) # x is a python dictionary in this case
    return x

def save_preference(preference_name,preference_value):
    try:
        file = read_json_file(PREFERENCES_FILE_NAME)
        file[preference_name]=preference_value
        return save_json_file(PREFERENCES_FILE_NAME,file)    
    except FileNotFoundError:
        print(save_preference,'ERROR Create preferences file')
        return False

def get_preference():
    try:
        return read_json_file(PREFERENCES_FILE_NAME)
    except FileNotFoundError:
        print(get_preference,'ERROR Create preferences file')
        return False

def create_preferences_init():
    preferences={
        "init": 0,
        # "usePreInstalledPython": True,
        "selected_lang": "en_EN",

    }
    def create_preferences(preferences):
        save_json_file(PREFERENCES_FILE_NAME,preferences)
    try:
        preferences_file = read_json_file(PREFERENCES_FILE_NAME)
        if preferences_file['init']:
            create_preferences(preferences)
            save_preference('init',0)
        else: 
            # print(create_preferences,'preferences file initialized')
            pass
    except FileNotFoundError:
        # print('creating preferences file')
        create_preferences(preferences)
        save_preference('init',0)
        # print(create_preferences,'preferences file initialized')

def load_preference(preference_key):
    preference = get_preference()
    try:
        preference_value=preference[preference_key]
        return preference_value
    except KeyError as e:
        print('setup','preference not set yet',preference_key)  

# def save_preference(values,preference_key):
#     preference_value = values[f'-{preference_key}-']
#     # print(save_preference,'preference_value',preference_value)
#     save_preference(preference_key,preference_value)         