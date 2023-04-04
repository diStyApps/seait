import PySimpleGUI as sg
import os
from threading import Thread
from datetime import datetime as dt
import subprocess
import requests
import re
import webbrowser
import threading
from util.ui_flattener import flatten_ui_elements
import util.colors as color
import util.icons as ic
import util.dependency_check as depcheck
from util.CONSTANTS import *
from util.apps_data import apps
import util.json_tools as jt
import util.app_func as app_func
import util.update_check_temp as update_check
import util.support as support
import util.repos as repos
import util.system_stats as system_stats
import time

sg.set_options(
    # button_color=('white', 'green'),
    # element_size=(50, 20),
    # auto_size_buttons=True,
    # font=('Helvetica', 14),
    # background_color='lightgray',
    # text_color='black',
    suppress_error_popups = True,
)

__version__ = '0.0.3'
APP_TITLE = f"Super Easy AI Installer Tool - Ver {__version__}"
# sg.theme('Dark Gray 15')
python_ver = depcheck.check_python()
git_ver = depcheck.check_git()
usePreInstalledPython=True
app_args = {
    1: ['--autolaunch', '--theme=dark'],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
}
# jt.create_preferences_init()
# jt.save_preference('usePreInstalledPython',usePreInstalledPython) 

def repack(widget, option):
    pack_info = widget.pack_info()
    pack_info.update(option)
    widget.pack(**pack_info)

def configure_canvas(event, canvas, frame_id):
    canvas.itemconfig(frame_id, width=canvas.winfo_width())

def configure_frame(event, canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def expand_column_helper(column):
    frame_id, frame, canvas = column.frame_id, column.TKFrame, column.canvas
    canvas.bind("<Configure>", lambda event, canvas=canvas, frame_id=frame_id:configure_canvas(event, canvas, frame_id))

def isfile_exist_check(file_path):
    if os.path.isfile(file_path):
        # print('isfile_exist_check:',file_path, ' FILE EXIST')
        return True
    if not os.path.isfile(file_path):
        # print('isfile_exist_check:',file_path,' FILE NOT EXIST')    
        return False   
    
def isfolder_exist_check(file_path):
    if os.path.exists(file_path):
        # print('isfolder_exist_check:',file_path, ' FOLDER EXIST')
        return True
    if not os.path.exists(file_path):
        # print('isfolder_exist_check:',file_path,' FOLDER NOT EXIST')    
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
        # pass

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

def update_app_args(app_id, arg_name):
    if app_id not in app_args:
        app_args[app_id] = []

    if arg_name in app_args[app_id]:
        app_args[app_id].remove(arg_name)
    else:
        app_args[app_id].append(arg_name)

def get_app_by_id(apps, app_id):
    for app in apps:
        if app.get("id") == app_id:
            return app
    return None

def is_update_available(current_version):
    url = "https://api.github.com/repos/diStyApps/Stable-Diffusion-Pickle-Scanner-GUI/releases/latest"
    response = requests.get(url)
    
    if response.status_code == 200:
        latest_release = response.json()
        latest_version = latest_release["tag_name"]
        print(f"Latest version: {latest_version}")
        return latest_version > current_version, latest_version
    else:
        raise Exception(f"Failed to fetch latest release information (status code: {response.status_code})")

def get_id(event):
    return int(re.search(r"_\d+", event).group(0)[1:])

def main():
    stop_event = threading.Event()

    #region layout
    top_column = [
        [
            sg.Frame('',[       
                    [
                        sg.Button("Installer",k=INSTALLS_TAB_KEY,font=FONT,expand_x=True,size=(15,2),button_color=(color.DARK_GRAY,color.DARK_BLUE),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                        sg.Button("Launcher",k=LAUNCHER_TAB_KEY,disabled=False,font=FONT,expand_x=True,size=(15,2),button_color=(color.DARK_BLUE,color.DARK_GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                        sg.Button("System Monitor",disabled=False,k=SYSTEM_STATS_TAB_KEY,font=FONT,expand_x=True,size=(20,2),button_color=(color.DARK_BLUE,color.DARK_GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                        sg.Button("AiPanic",disabled=True,k=AIPANIC_TAB_KEY,font=FONT,expand_x=True,size=(10,2),button_color=(color.DARK_BLUE,color.DARK_GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                        sg.Button("About",k=ABOUT_TAB_KEY,font=FONT,expand_x=False,size=(10,2),button_color=(color.DARK_BLUE,color.DARK_GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                        sg.Button("EN",disabled=True,k=GPU_TAB_KEY,font=FONT,expand_x=False,size=(5,2),button_color=(color.DARK_BLUE,color.DARK_GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                    ],                   
            ],expand_x=True,expand_y=False,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.GRAY_9900)        
        ]
    ]
    
    bottom_column = [
        [
            sg.Frame('',[       
                    [
                        # cpbar.progress_bar_custom_layout(PBAR_KEY,visible=True,it_name="file")
                    ],
            ],expand_x=True,border_width=0,relief=sg.RELIEF_FLAT,element_justification='c')
        ],    
    ]

    install_tab_column_left = [
        [
            sg.Frame('',[ 
        #seait
        [
            sg.Frame('',[       
                [
                    sg.Button(f"Installed version: {__version__}",k=UPDATE_AVAILABLE_LBL_KEY,font=FONT,expand_x=True,size=(30,2),disabled=True),
                ],                
                [
                    sg.Button("Check for update",k=UPDATE_BTN_KEY,font=FONT,expand_x=True,size=(20,1),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                ],                                                          
            ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
        ],    
        #Python
        [
            sg.Frame('',[       
                        [
                            sg.Image(data=ic.python,background_color=color.DARK_GRAY),
                            sg.Text("Python",font=FONT,background_color=color.DARK_GRAY),
                        ],  
                [
                    sg.Button("Pre Installed - 3.10.6",visible=False,key=DEP_APP_PRE_INSTALLED_VERSION_LBL_KEY,font=FONT,expand_x=True,size=(20,2),disabled=True),
                    sg.Button(f"{python_ver}",k=DEP_APP_PYTHON_INSTALLED_VERSION_LBL_KEY,font=FONT,expand_x=True,size=(30,2),disabled=True),
                ],               
                [
                    sg.Button("Use pre installed",visible=False,k=DEP_APP_PYTHON_USE_PRE_INSTALL_KEY,font=FONT,expand_x=True,size=(20,1),button_color=(color.LIGHT_BLUE,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                    sg.Button("Install",k=DEP_APP_PYTHON_INSTALL_KEY,font=FONT,expand_x=True,size=(30,1),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                    # sg.Button("Locate",k="setup",font=FONT,expand_x=True,size=(10,1),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                ],                                          
            ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
        ],                 
        #Git
        [
            sg.Frame('',[       
                        [
                            sg.Image(data=ic.git,background_color=color.DARK_GRAY),
                            sg.Text("Git",font=FONT,background_color=color.DARK_GRAY),
                        ],  
                [
                    # sg.Button("Installed Version",k="setup",font=FONT,expand_x=True,size=(20,2),disabled=True),
                    sg.Button(git_ver ,k=DEP_APP_GIT_INSTALLED_VERSION_LBL_KEY,font=FONT,expand_x=True,size=(40,2),disabled=True),
                ],                
                [
                            sg.Button("Install",k=DEP_APP_GIT_INSTALL_KEY,font=FONT,expand_x=True,size=(10,1),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                            # sg.Button("Locate",k="setup",font=FONT,expand_x=True,size=(10,1),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                            # sg.Button("Refresh",k="setup",font=FONT,expand_x=True,size=(10,1),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                ],                                          
            ],expand_x=True,expand_y=False,key=DEP_APP_GIT_INSTALLED_VERSION_FRAME_KEY,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
        ],                              
            ],expand_x=True,expand_y=True,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color="#2A2929")
        ],  
    ]

    install_tab_column_right = [   
        [
            sg.Frame("",layout=[
                    [
                        sg.Frame("",[       
                                [
                                    sg.Image(app["image_path"],background_color=color.DARK_GRAY),
                                    sg.Text(app["title"],font=FONT,background_color=color.DARK_GRAY),
                                    sg.Push(background_color=color.DARK_GRAY),
                                    # sg.Button("",k="setup",size=(3,1),font=FONT,mouseover_colors=(color.GRAY_9900,color.DARK_GREEN),button_color=(color.GRAY_9900,color.GRAY)),
                                ],
                                [
                                    sg.Button(app['github_url'],k=f"-app_{app['id']}_install_tab_installed_github_lbl_key-",font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN),disabled=False),
                                ], 
                                [
                                    sg.Button("Installed Version",visible=True,font=FONT,expand_x=True,size=(20,1),disabled=True),
                                    # sg.Button(app['installed_version'],visible=False,k=f"-lbl_app_{app['id']}_install_tab_installed_version_lbl_key-",size=(40,1),font=FONT,expand_x=True,disabled=True)
                                    sg.Button(get_last_commit_hash_local(app),visible=True,k=f"-lbl_app_{app['id']}_install_tab_installed_version_lbl_key-",size=(40,1),font=FONT,expand_x=True,disabled=True)
                                    # sg.Button(get_last_commit_hash_local(f"{app['webui_path']}\extensions\{app['repo_name']}"),visible=False,k=f"-lbl_app_{app['id']}_install_tab_installed_version_lbl_key-",size=(40,1),font=FONT,expand_x=True,disabled=True)
                                ],  
                                [
                                    sg.Button("Available Version",visible=False,font=FONT,expand_x=True,size=(20,1),disabled=True),
                                    sg.Button(get_last_commit_hash_remote(app['github_url']),visible=False,size=(40,1),k=f"-lbl_app_{app['id']}_install_tab_installed_version_lbl_key-",font=FONT,expand_x=True,disabled=True),
                                ],  
                                [
                                    sg.Button(button['button_text'],disabled=False, key=f"-app_{app['id']}_{button['key']}_install_tab_btn-",font=FONT,expand_x=True,mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)) 
                                    for button in app['buttons'] if app['status']
                                ]                              
                            ],expand_x=True,expand_y=True,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
                    ]
                ],expand_x=True,expand_y=True,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.GRAY
            )
        ]
        for app in apps if app['visible']
    ]

    install_tab_column_right_scrollable = [
        [
            sg.Column(install_tab_column_right, key=C2_INSTALLS_KEY, element_justification='l', expand_x=True,expand_y=True,visible=True,scrollable=True,vertical_scroll_only=True),
        ],
    ]

    launcher_column_left = [
        [
            sg.Frame('',[ 
                [
                    sg.Frame('',[       
                        [
                            sg.Image(app["image_path"],background_color=color.DARK_GRAY),
                            sg.Text(app["title"],font=FONT,background_color=color.DARK_GRAY),
                        ],  
                        [
                            sg.Button(get_last_commit_hash_local(app),k="setup",font=FONT,expand_x=True,size=(40,2),disabled=True),
                        ],                      
                        [
                            sg.Button(button['button_text'], key=f"-applauncher_{app['id']}_{button['key']}_launcher_tab_btn-",font=FONT,expand_x=True,mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)) 
                            for button in app['launch_buttons']
                        ]                                  
                    ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
                ],   
                [
                    sg.Frame('',[       
                        [
                            sg.Image(ic.args,background_color=color.DARK_GRAY,size=(30,30)),
                            sg.Text("Arguments",font=FONT,background_color=color.DARK_GRAY),
                        ],  
                    ],expand_x=True,expand_y=False,border_width=0,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)            
                ],          
                [
                    sg.Frame('',[                                 
                        [
                            sg.Button(option["button_text"], key=f"-appargs_{app['id']}_{option['button_text']}_launcher_tab_btn-", font=FONT, expand_x=True,
                                    mouseover_colors=(color.GRAY_9900, color.DARK_GREEN)) for option in arg
                        ]
                        for arg in app['args']
                    ],expand_x=True,expand_y=True,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
                ],                           
            ],expand_x=True,expand_y=True,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.GRAY)
        for app in apps if app['type'] == "app"
        ]
        # for app in apps if app['type'] == "app" #vertical
    ]
   
    system_stats_tab_column = [
        [
            sg.Frame('',[ 
                [
                    sg.Frame('',[ 

                        # [
                        #     sg.Button("Start",key="-start_monitor-",size=(15,1),font=FONT,expand_x=True,expand_y=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=False),

                        #     sg.Button("Update Interval",key="-start_monitor-",font=FONT,expand_x=True,expand_y=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=False),

                        #     sg.In("1",font=FONT,size=(5,1),expand_x=True,expand_y=True,justification="c",background_color=color.LIGHT_GRAY),   
                        # ],
                        # [
                        #     # sg.Button("",key=SYSTEM_STATS_CPU_USAGE_PRECENT_LBL_KEY,size=(40,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
                        #     # sg.Button("1",size=(20,2),font=FONT,expand_x=True,expand_y=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=False),
                        #     sg.Slider(range=(0, 10), orientation='h',
                        #         key='-slider-',size=(20,15),expand_x=True,disable_number_display=True,visible=True,background_color=color.LIGHT_GRAY),
                        #     sg.Button("Start",size=(15,2),font=FONT,expand_x=True,expand_y=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=False),
                        # ],         
                        [
                            sg.Button("CPU Usage",size=(15,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
                            sg.Button("",key=SYSTEM_STATS_CPU_USAGE_PRECENT_LBL_KEY,size=(40,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
                        ],                         
                        [
                            sg.Button("RAM Usage",size=(15,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),        
                            sg.Button("",key=SYSTEM_STATS_RAM_USAGE_LBL_KEY,size=(40,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
                        ],                                     
                    ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.DARK_GRAY)
                ],                                  
            ], expand_x=True, expand_y=False, border_width=5, pad=(10,10), relief=sg.RELIEF_FLAT, element_justification="c", background_color=color.DARK_GRAY)
        ],  
    ]

    gpu_stats = system_stats.get_gpu_stats()
    for i, gpu_stat in enumerate(gpu_stats):
        system_stats_tab_column.append([
            sg.Frame('',[
                [
                    sg.Text(gpu_stat['name'], key=f"-{SYSTEM_STATS_GPU_NAME_LBL_KEY}_{i}-", font=FONT_H1, background_color=color.DARK_GRAY, text_color=color.LIGHT_GRAY),
                ],
                [
                    sg.Frame("",[       
                            [
                                sg.Button("Temperature",size=(15,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
            
                                sg.Button('', key=f"-{SYSTEM_STATS_GPU_TEMP_LBL_KEY}_{i}-",size=(40,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
                            ], 
                            [
                                sg.Button("VRAM Usage",size=(15,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
                                sg.Button(f"",size=(40,2), key=f"-{SYSTEM_STATS_GPU_VRAM_LBL_KEY}_{i}-",font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
                            ],                                 
                            [
                                sg.Button("Power Usage",size=(15,2),font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
            
                                sg.Button(f"",size=(40,2), key=f"-{SYSTEM_STATS_GPU_POWER_USAGE_LBL_KEY}_{i}-",font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True),
                            ],                              
                        ],expand_x=True,expand_y=True,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
                ]
            ], expand_x=True, expand_y=False, border_width=5, pad=(10,10), relief=sg.RELIEF_FLAT, element_justification="c", background_color=color.DARK_GRAY)
        ])


    about_tab_column = [
            [
                sg.Frame('',[ 
                    [
                        sg.Frame('',[       
                            [
                                sg.Image(ic.avatar2,background_color=color.DARK_GRAY),
                            ],                             
                            [
                                sg.Text("diSty",font=FONT,background_color=color.DARK_GRAY,text_color=color.LIGHT_GRAY),
                            ],
                            [support.buttons_layout()],
                            [
                                sg.Text("Don't forget to leave a star.",font=FONT,background_color=color.DARK_GRAY,text_color=color.DIM_GREEN),
                            ],                            
                            [repos.buttons_layout()],    
                            [
                                sg.Text("Progress is impossible without change, and those who cannot change their minds cannot change anything.",
                                        font=FONT,background_color=color.DARK_GRAY,text_color=color.GRAY),
                            ],    
                        ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.DARK_GRAY)
                    ],                                  
                ],expand_x=True,expand_y=True,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color="#2A2929")
            ],  
        ]

    layout = [[ 
            [
                top_column, 
            ],
            [
                sg.Column(install_tab_column_left, key=C1_INSTALLS_KEY, element_justification='l', expand_x=True,expand_y=True,visible=True,scrollable=False,vertical_scroll_only=True),
                sg.Column(install_tab_column_right_scrollable, key=INSTALL_COLUMN_LEFT_SCROLLABLE_KEY, element_justification='l', expand_x=True,expand_y=True,visible=True),
                sg.Column(launcher_column_left, key=C1_LAUNCH_KEY, element_justification='l', expand_x=True,expand_y=True,visible=False),
                sg.Column(about_tab_column, key=C1_ABOUT_KEY, element_justification='c', expand_x=True,expand_y=True,visible=False),
                sg.Column(system_stats_tab_column, key=C1_SYSTEM_STATS_KEY, element_justification='c', expand_x=True,expand_y=True,visible=False),
            ],        
            [
                bottom_column,
            ],
    ]]

    #endregion layout

    window = sg.Window(APP_TITLE,layout,finalize=True, resizable=True,enable_close_attempted_event=False,background_color=color.GRAY_9900)
    # window.Maximize()    
    window.set_min_size((500,300))

    c1_install_col:sg.Column = window[C1_INSTALLS_KEY]
    c2_install_col_scroll:sg.Column = window[INSTALL_COLUMN_LEFT_SCROLLABLE_KEY]
    c1_launcher_col:sg.Column = window[C1_LAUNCH_KEY]
    c1_about_col:sg.Column = window[C1_ABOUT_KEY]
    c1_system_stats_col:sg.Column = window[C1_SYSTEM_STATS_KEY]
    c2_install_widget:sg.Column = window[C2_INSTALLS_KEY].widget
    install_tab_btn_elem:sg.Button = window[INSTALLS_TAB_KEY]
    launcher_tab_btn_elem:sg.Button = window[LAUNCHER_TAB_KEY]
    about_tab_btn_elem:sg.Button = window[ABOUT_TAB_KEY]
    system_stats_tab_btn_elem:sg.Button = window[SYSTEM_STATS_TAB_KEY]
    use_python_pre_install_btn_elem:sg.Button = window[DEP_APP_PYTHON_USE_PRE_INSTALL_KEY]
    install_python_btn_elem:sg.Button = window[DEP_APP_PYTHON_INSTALL_KEY]
    install_git_btn_elem:sg.Button = window[DEP_APP_GIT_INSTALL_KEY]
    installed_version_python_lbl_elem:sg.Text = window[DEP_APP_PYTHON_INSTALLED_VERSION_LBL_KEY]
    installed_git_version_lbl_elem:sg.Text = window[DEP_APP_GIT_INSTALLED_VERSION_LBL_KEY]
    pre_installed_version_lbl_elem:sg.Button = window[DEP_APP_PRE_INSTALLED_VERSION_LBL_KEY]
    update_available_lbl_elem:sg.Text = window[UPDATE_AVAILABLE_LBL_KEY]

    tab_elements = {
        INSTALLS_TAB_KEY: [c1_install_col, c2_install_col_scroll],
        LAUNCHER_TAB_KEY: [c1_launcher_col],
        ABOUT_TAB_KEY: [c1_about_col],
        SYSTEM_STATS_TAB_KEY: [c1_system_stats_col]
    }

    tab_btn_elements = {
        INSTALLS_TAB_KEY: install_tab_btn_elem,
        LAUNCHER_TAB_KEY: launcher_tab_btn_elem,
        ABOUT_TAB_KEY: about_tab_btn_elem,
        SYSTEM_STATS_TAB_KEY: system_stats_tab_btn_elem
    }

    def convert_button_disable():
        use_python_pre_install_btn_elem.update(button_color=(color.LIGHT_BLUE,color.GRAY))

    def convert_button_enable():
        use_python_pre_install_btn_elem.update(button_color=(color.GRAY_9900,color.DARK_GREEN))

    def dialog_window(title,method):
            event, values = sg.Window('', 
            [
                [
                    sg.Frame('',[
                        [
                            sg.Button(f'{method} {title} ?',expand_x=True,expand_y=True,font=("Arial", 18, "bold"),disabled_button_color=(color.LIGHT_BLUE, color.DARK_GRAY),disabled=True,border_width=0),
                        ],                        
                        [
                            sg.Button('Yes',expand_x=True,expand_y=True,s=(5,2),font=("Arial", 14, "bold"),button_color=(color.DIM_GREEN,color.DARK_GRAY),border_width=0),
                            sg.Button('No',expand_x=True,expand_y=True,s=(5,2),font=("Arial", 14, "bold"),button_color=(color.RED_ORANGE, color.DARK_GRAY),border_width=0)
                        ],

                    ],expand_x=True,expand_y=True,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.LIGHT_GRAY)                       
                ]
            ],
                modal=True, element_justification='c',no_titlebar=True,background_color=color.DARK_GRAY,auto_size_text=True,).read(close=True)
            if event == 'Yes':
                return True
            if event == 'No':
                return False

    def git_event_handler():
        if depcheck.check_git():
            install_git_btn_elem.update("Installed",disabled_button_color=(color.DARK_GREEN,color.DARK_GREEN),disabled=True)   
        else:
            install_git_btn_elem.update("Install",disabled=False)
            installed_git_version_lbl_elem.update(disabled_button_color=(color.GRAY,color.GRAY),button_color=(color.RED_ORANGE,color.RED_ORANGE),disabled=True)

    def python_event_handler():
        if depcheck.check_python():
            install_python_btn_elem.update("Installed",disabled_button_color=(color.DARK_GREEN,color.DARK_GREEN),disabled=True)   
        else:
            install_python_btn_elem.update("Install",disabled=False)
            installed_version_python_lbl_elem.update(disabled_button_color=(color.GRAY,color.GRAY),button_color=(color.RED_ORANGE,color.RED_ORANGE),disabled=True)
            if isfolder_exist_check(app_func.pre_installed_python_path):
                app_func.usePreInstalledPython = not app_func.usePreInstalledPython
                convert_button_enable() if app_func.usePreInstalledPython else convert_button_disable()

        if isfolder_exist_check(app_func.pre_installed_python_path):
            # print("pre installed python found")
            app_func.usePreInstalledPython = not app_func.usePreInstalledPython
            convert_button_enable() if app_func.usePreInstalledPython else convert_button_disable()
        else:
            # print("pre installed python not found")         
            pre_installed_version_lbl_elem.update("Pre installed")
            use_python_pre_install_btn_elem.update(disabled_button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True)

    def change_btn_state(x,staus):
        for widget_key,v in window.key_dict.items():
            if str(widget_key).startswith(x):
                window[widget_key].update(disabled=staus) 

    def check_installation_status(app):
        project_path = os.path.abspath(app['repo_name'])
        if app['type'] == "app":
            install_btn = window[f"-app_{app['id']}_install_install_tab_btn-"]
            uninstall_btn = window[f"-app_{app['id']}_uninstall_install_tab_btn-"]
            update_btn = window[f"-app_{app['id']}_update_install_tab_btn-"]
            create_venv_btn = window[f"-app_{app['id']}_create_venv_install_tab_btn-"]
            delete_venv_btn = window[f"-app_{app['id']}_delete_venv_install_tab_btn-"]
            update_btn = window[f"-app_{app['id']}_update_install_tab_btn-"]
            if isfolder_exist_check(project_path):
                install_btn.update(disabled=True)
                uninstall_btn.update(disabled=False)
                update_btn.update(disabled=False)
                # launcher_tab_btn_elem.update(disabled=False)
                # print("webui installed")
                if isfolder_exist_check(os.path.join(project_path, 'venv')):
                    create_venv_btn.update(disabled=True)
                    delete_venv_btn.update(disabled=False)
                    # print("venv installed")      
                else:
                    # print("venv not installed")    
                    create_venv_btn.update(disabled=False)
                    delete_venv_btn.update(disabled=True)
            else:
                install_btn.update(disabled=False)
                uninstall_btn.update(disabled=True)
                delete_venv_btn.update(disabled=True)
                create_venv_btn.update(disabled=True)
                update_btn.update(disabled=True)
                # change_btn_state('-app_2_',True)
                # change_btn_state('-app_3_',True)

        if app['type'] == "webui_extension":
            if app['buttons']:
                update_extension_btn = window[f"-app_{app['id']}_update_webui_extension_install_tab_btn-"]
                uninstall_extension_btn = window[f"-app_{app['id']}_uninstall_webui_extension_install_tab_btn-"]
                install_extension_btn = window[f"-app_{app['id']}_install_webui_extension_install_tab_btn-"]
                install_extension_btn = window[f"-app_{app['id']}_install_webui_extension_install_tab_btn-"]

                
                if isfolder_exist_check(f"{app['webui_path']}\extensions\{app['repo_name']}"):
                    # print(f"{app['repo_name']} is installed")
                    install_extension_btn.update(disabled=True)
                    update_extension_btn.update(disabled=False)
                    uninstall_extension_btn.update(disabled=False)
                    
                else:
                    # print(f"{app['webui_path']}\extensions\{app['repo_name']}")
                    # print(f"{app['repo_name']} is not installed")
                    install_extension_btn.update(disabled=False)
                    update_extension_btn.update(disabled=True)
                    uninstall_extension_btn.update(disabled=True)

    def system_stats_monitor(stop_event,update_interval=1):
            while not stop_event.is_set():
                window[SYSTEM_STATS_CPU_USAGE_PRECENT_LBL_KEY].update(f"{system_stats.get_cpu_stats()['cpu_percent']} %")
                window[SYSTEM_STATS_RAM_USAGE_LBL_KEY].update(f"{system_stats.get_ram_stats()['ram_used']} / {system_stats.get_ram_stats()['ram_total']}") 
                for i, gpu_stat in enumerate(system_stats.get_gpu_stats()):
                    window[f"-{SYSTEM_STATS_GPU_NAME_LBL_KEY}_{i}-"].update(gpu_stat['name'])
                    window[f"-{SYSTEM_STATS_GPU_TEMP_LBL_KEY}_{i}-"].update(f"{gpu_stat['temperature']} °C")
                    window[f"-{SYSTEM_STATS_GPU_POWER_USAGE_LBL_KEY}_{i}-"].update(f"{gpu_stat['power_usage']:.2f} / {gpu_stat['card_power']:.2f}  W")
                    window[f"-{SYSTEM_STATS_GPU_VRAM_LBL_KEY}_{i}-"].update(f"{gpu_stat['vram_used']} / {gpu_stat['vram_total']}")            
            time.sleep(update_interval)

    def default_lancher_buttons():
        window["-appargs_1_--theme=dark_launcher_tab_btn-"].update(button_color=(color.GRAY_9900,color.DARK_GREEN))
        window["-appargs_1_--autolaunch_launcher_tab_btn-"].update(button_color=(color.GRAY_9900,color.DARK_GREEN))

    def handle_tab_event(event, tab_elements, tab_btn_elements, active_color, inactive_color):
        if event == "-system_stats_tab-":
            stop_event.clear()
            t = threading.Thread(target=system_stats_monitor, args=(stop_event,1,))
            t.start()
        else:
            stop_event.set()

        for tab_key in tab_elements:
            is_target = tab_key == event
            for element in tab_elements[tab_key]:
                element.update(visible=is_target)
            tab_btn_elements[tab_key].update(button_color=(active_color if is_target else inactive_color))

    active_color = (color.DARK_GRAY, color.DARK_BLUE)
    inactive_color = (color.DARK_BLUE, color.DARK_GRAY)

    expand_column_helper(c2_install_widget)
    flatten_ui_elements(window)
    git_event_handler()
    python_event_handler()
    default_lancher_buttons()

    for app in apps:
        check_installation_status(app)

    while True:
        event, values = window.read()
        # print('main','event',event,'values',values)
        if event == sg.WIN_CLOSED:
            break

        if event == DEP_APP_PYTHON_USE_PRE_INSTALL_KEY:
            app_func.usePreInstalledPython = not app_func.usePreInstalledPython
            convert_button_enable() if app_func.usePreInstalledPython else convert_button_disable()

        if event == DEP_APP_PYTHON_INSTALL_KEY:
            if isfile_exist_check(INSTALLERS_PYTHON_PATH):
                subprocess.run([INSTALLERS_PYTHON_PATH]) 
                installed_version_python_lbl_elem.update(python_ver)
                python_event_handler()
            else:
                installed_version_python_lbl_elem.update("Download the installers version")

        if event == DEP_APP_GIT_INSTALL_KEY:
            if isfile_exist_check(INSTALLERS_GIT_PATH):
                subprocess.run([INSTALLERS_GIT_PATH])
                installed_git_version_lbl_elem.update(git_ver)
                git_event_handler()
            else:
                installed_git_version_lbl_elem.update("Download the installers version")

        if event in tab_elements:
            handle_tab_event(event, tab_elements, tab_btn_elements, active_color, inactive_color)
   
        if event.startswith("-app_") and event.endswith("_btn-"):
            id_number = get_id(event)
            method = re.search(r"-app_\d+_(.+)_install_tab_btn-", event).group(1) 
            app_info = get_app_by_id(apps, id_number)
            # if method != "install" or method != "install_webui_extension":
            if dialog_window(app_info['title'],method):
                if method == "install":
                    window[f"-app_{app_info['id']}_install_install_tab_btn-"].update("Installing",disabled=True)
                    
                    Thread(target=app_func.methods[method], args=(app_info,app_args[id_number],), daemon=True).start() 
                else:
                    app_func.methods[method](app_info)
                    check_installation_status(app_info)

        if event.startswith("-applauncher_") and event.endswith("_btn-"):
            id_number = int(re.search(r"_\d+", event).group(0)[1:])
            method = re.search(r"-applauncher_\d+_(.+)_launcher_tab_btn-", event).group(1)   
            
            app_info = get_app_by_id(apps, id_number)
            Thread(target=app_func.methods[method], args=(app_info,app_args[id_number],), daemon=True).start() 
            window[f"-applauncher_{id_number}_launch_launcher_tab_btn-"].update("Launched",button_color=(color.GRAY_9900,color.DARK_GREEN),disabled=True)

        if event.startswith("-appargs_") and event.endswith("_btn-"):
            id_number = get_id(event)
            method = re.search(r"-appargs_\d+_(.+)_launcher_tab_btn-", event).group(1)   
            update_app_args(id_number,method)
            if window[event].ButtonColor[0] == color.GRAY_9900:
                window[event].update(button_color=(color.LIGHT_BLUE,color.GRAY))
            else:
                window[event].update(button_color=(color.GRAY_9900,color.DARK_GREEN))

        if event.startswith("-app_") and event.endswith("_install_tab_installed_github_lbl_key-"):
            id_number = get_id(event)
            webbrowser.open(get_app_by_id(apps, id_number)['github_url'])  

        if event == UPDATE_BTN_KEY:
            if not update_check.check_update_available(__version__).startswith("No update available"):
                update_available_lbl_elem.update(update_check.check_update_available(__version__),button_color=(color.GRAY_9900,color.DARK_GREEN),disabled=False)
            else:
                update_available_lbl_elem.update(update_check.check_update_available(__version__))

        if event == UPDATE_AVAILABLE_LBL_KEY:
            webbrowser.open(LATEST_RELEASE_URL)  
        support.buttons(event)
        repos.buttons(event)

        if event == "-start_monitor-":
            Thread(target=system_stats_monitor, args=(), daemon=True).start() 

if __name__ == '__main__':

    main() 
