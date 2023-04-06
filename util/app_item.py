import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *
import util.dependency_check as depcheck
import os
import util.colors as color
import util.icons as ic

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
        # pass

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

def check_installation_status(project):
    project_path = os.path.abspath(project['repo_name'])
    if project['type'] == "app":
        if is_folder_exist_check(project_path):
            print(f"{project['repo_name']} project installed")      
            if is_folder_exist_check(os.path.join(project_path, 'venv')):
                print(f"{project['repo_name']} venv installed")
                return True
            else:
                print(f"{project['repo_name']} venv not installed")
                return False
        else:
            print(f"{project['repo_name']} project not installed")
            return False
    elif project['type'] == "webui_extension":
        if is_folder_exist_check(f"{project['webui_path']}\extensions\{project['repo_name']}"):
            print(f"extension {project['repo_name']} is installed")
            return True
        else:
            print(f"extension {project['repo_name']} is not installed")
            return False
        
def check_installation_git_Python_status():
    if depcheck.check_python() and depcheck.check_git():
        print("Python and git installed")
        return True  
    else:
        print("Python or git not installed")
        return False        
    
def layout(app):
    main_key = '-selected_app_'
    selected_app_key = f"{main_key}{app['id']}_"
    installation_status = check_installation_status(app)
    git_Python_status = check_installation_git_Python_status()
    app_commit_hash = get_last_commit_hash_local(app)
    launcher_column_right = [
        [
            sg.Frame('',[        
                [
                    sg.Image(app['image_path'],key=f"{main_key}img-",background_color=color.DARK_GRAY),
                    sg.Text(app['title'],key=f"{main_key}name-",font=FONT,background_color=color.DARK_GRAY),
                    sg.Push(background_color=color.DARK_GRAY),
                ],        
                [
                    sg.Button(app['github_url'],k=f"{selected_app_key}github_btn-",font=FONT,expand_x=True,button_color=(color.DARK_BLUE,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_BLUE),disabled=False),
                ],                                         
                [
                    sg.Button("Installed Version",k=f"{main_key}github_lbl-",visible=True,font=FONT,expand_x=True,size=(20,1),disabled=True),
                    sg.Button(app_commit_hash,visible=True,k=f"-{selected_app_key}commit_hash_lbl-",size=(40,1),font=FONT,expand_x=True,disabled=True)
                ],                        
                [ 
                    # sg.Button(button['button_text'],disabled=False,button_color=(color.DIM_GREEN,color.GRAY), key=f"{main_key}func_{app['id']}_{button['key']}_btn-",font=FONT,expand_x=True,mouseover_colors=(color.GRAY_9900,color.DIM_GREEN)) 
                    sg.Button(app['launch_buttons'][0]['button_text'],disabled=False if git_Python_status else True,button_color=(color.DIM_GREEN,color.GRAY), key=f"{main_key}func_{app['id']}_{app['launch_buttons'][0]['key']}_btn-",font=FONT_H1,expand_x=True,mouseover_colors=(color.GRAY_9900,color.DIM_GREEN)) 
                   
                    # for button in app['launch_buttons']
                ] if installation_status else [
                    # sg.Button(button['button_text'],disabled=True,button_color=(color.DIM_GREEN,color.GRAY), key=f"{main_key}func_{app['id']}_{button['key']}_btn-",font=FONT,expand_x=True,mouseover_colors=(color.GRAY_9900,color.DIM_GREEN)) 
                    sg.Button(app['launch_buttons'][1]['button_text'],disabled=False if git_Python_status else True,button_color=(color.DIM_GREEN,color.GRAY), key=f"{main_key}func_{app['id']}_{app['launch_buttons'][1]['key']}_btn-",font=FONT_H1,expand_x=True,mouseover_colors=(color.GRAY_9900,color.DIM_GREEN)) 
                    # for button in app['launch_buttons']
                ]
                                  
            ],key=f'{main_key}frame-',expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
        ],   
        [
            sg.Frame("",[       
                [
                    sg.Frame('',[       
                        [
                            sg.Image(ic.args,key=f"{main_key}args_img-",background_color=color.DARK_GRAY,size=(30,30)),
                            sg.Text("Arguments",key=f"{main_key}args_lbl-",text_color=color.LIGHT_GRAY,font=FONT,background_color=color.DARK_GRAY),
                        ],  
                    ],key=f"{main_key}args_header_frame-",expand_x=True,expand_y=False,border_width=0,pad=(10,3),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)            
                ],  
                [
                    sg.Frame('',[  
                        [
                            sg.Button(option["button_text"],disabled=False,size=(24,1),button_color=(color.DIM_GREEN,color.GRAY), key=f"{main_key}args_{app['id']}_{option['button_text']}_btn-", font=FONT, expand_x=True,
                                    mouseover_colors=(color.GRAY_9900,color.DIM_GREEN)) for option in arg
                        ]
                        for arg in app['args']
                    ],key=f"{main_key}args_frame-",expand_x=True,expand_y=False,border_width=5,pad=(10,0),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
                ],                            
                ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
        ] if app['args'] else [],    
        [
            sg.Frame("",[       
                [
                    sg.MLine("",k=f"{main_key}args_{app['id']}_console_ml-",visible=True,text_color=color.DIM_GREEN,border_width=10,sbar_width=20,sbar_trough_color=0,
                            autoscroll=True, auto_refresh=True,expand_x=True,expand_y=True,font=FONT,no_scrollbar=True,),
                ]                              
                ],key=f"{main_key}args_console_frame-",expand_x=True,expand_y=True,border_width=5,pad=(5,0),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.GRAY_1111)
        ] if app['args'] else [],
        [
            sg.Frame('',[       
            [
                sg.Frame('',[       
                    [
                        sg.Image(ic.args,key=f"{main_key}setup_img-",background_color=color.DARK_GRAY,size=(30,30)),
                        sg.Text("Setup",key=f"{main_key}setup_lbl-",text_color=color.LIGHT_GRAY,font=FONT,background_color=color.DARK_GRAY),
                    ],  
                ],key=f"{main_key}setup_header_frame-",expand_x=True,expand_y=False,border_width=0,pad=(10,3),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)            
            ],                
            [
                sg.Frame("",[       
                        [
                            sg.Button(button['button_text'],disabled=False, key=f"{main_key}func_{app['id']}_{button['key']}_btn-",font=FONT,expand_x=True,button_color=(color.DARK_BLUE,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_BLUE)) 
                            for button in app['buttons'] if app['status']
                        ]
                        if installation_status and git_Python_status else [
                           sg.Button(button['button_text'],disabled=True, key=f"{main_key}func_{app['id']}_{button['key']}_btn-",font=FONT,expand_x=True,button_color=(color.DARK_BLUE,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_BLUE)) 
                            for button in app['buttons'] if app['status']
                        ]                              
                ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
            ] 
            ],key=f"{main_key}setup_frame-",expand_x=True,expand_y=False,border_width=0,pad=(10,3),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)            
        ],             
       
    ]
    
    return launcher_column_right