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
        
def app_item_layout(app):
    launcher_column_right = [
        [
            sg.Frame('',[ 
                [
                    sg.Frame('',[        
                        [
                            sg.Image(app['image_path'],key="-selected_app_img-",background_color=color.DARK_GRAY),
                            sg.Text(app['title'],key="-selected_app_name-",font=FONT,background_color=color.DARK_GRAY),
                            sg.Push(background_color=color.DARK_GRAY),
                        ],        
                        [
                            sg.Button(app['github_url'],k=f"-selected_github_btn-",font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN),disabled=False),
                            # sg.Button(app['github_url'],k=f"-app_{app}_install_tab_installed_github_lbl_key-",font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN),disabled=False),
                        ],                                         
                        [
                            sg.Button("Installed Version",visible=True,font=FONT,expand_x=True,size=(20,1),disabled=True),
                            # sg.Button(get_last_commit_hash_local(app),visible=True,k=f"-lbl_app_{app}_install_tab_installed_version_lbl_key-",size=(40,1),font=FONT,expand_x=True,disabled=True),
                            sg.Button(get_last_commit_hash_local(app),visible=True,k=f"-selected_app_commit_hash_lbl-",size=(40,1),font=FONT,expand_x=True,disabled=True)
                        ],                        
                        [
                            sg.Button(button['button_text'], key=f"-applauncher_{app}_{button['key']}_launcher_tab_btn-",font=FONT,expand_x=True,mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)) 
                            for button in app['launch_buttons']
                        ]                                  
                    ],key='-launch_buttons_frame-',expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
                ],   
            ],expand_x=True,expand_y=False,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.GRAY)
        ],
        [
            sg.Frame("",[       
                [
                    sg.Frame('',[       
                        [
                            sg.Image(ic.args,background_color=color.DARK_GRAY,size=(30,30)),
                            sg.Text("Arguments",font=FONT,background_color=color.DARK_GRAY),
                        ],  
                    ],expand_x=True,expand_y=False,border_width=0,pad=(10,3),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)            
                ],  
                [
                    sg.Frame('',[  
                        [
                            sg.Button(option["button_text"],size=(24,1), key=f"-appargs_{app}_{option['button_text']}_launcher_tab_btn-", font=FONT, expand_x=True,
                                    mouseover_colors=(color.GRAY_9900, color.DARK_GREEN)) for option in arg
                        ]
                        for arg in app['args']
                    ],expand_x=True,expand_y=False,border_width=5,pad=(10,0),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
                ],                            
                ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
        ] if app['args'] else [],    
        [
            sg.Frame("",[       
                [
                ]                              
            ],expand_x=True,expand_y=True,border_width=0,relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.GRAY_1111)
        ],                 
        [
            sg.Frame("",[       
                [
                    sg.MLine("--xformers",k="CONSOLE_ML_KEY",visible=True,text_color=color.TERMINAL_GREEN2,border_width=10,sbar_width=20,sbar_trough_color=0,
                            autoscroll=True, auto_refresh=True,expand_x=True,expand_y=True,font=FONT,no_scrollbar=True,),
                ]                              
                ],expand_x=True,expand_y=True,border_width=5,pad=(5,0),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.GRAY_1111)
        ] if app['args'] else [],
        [
            sg.Frame("",[       
                    [
                        sg.Button("Available Version",visible=False,font=FONT,expand_x=True,size=(20,1),disabled=True),
                        # sg.Button(get_last_commit_hash_remote(app['github_url']),visible=False,size=(40,1),k=f"-lbl_app_{app}_install_tab_installed_version_lbl_key-",font=FONT,expand_x=True,disabled=True),
                    ],  
                    [
                        sg.Button(button['button_text'],disabled=False, key=f"-app_{app}_{button['key']}_install_tab_btn-",font=FONT,expand_x=True,mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)) 
                        for button in app['buttons'] if app['status']
                    ]                              
            ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
        ]        
    ]
    
    return launcher_column_right