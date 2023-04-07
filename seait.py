import PySimpleGUI as sg
import os
from threading import Thread
import subprocess
import re
import time
import webbrowser
import threading
from util.ui_tools import flatten_ui_elements,expand_column_helper,clear_items_keys
import util.colors as color
import util.icons as ic
import util.dependency_check as depcheck
from util.CONSTANTS import *
from util.projects_data import projects
# import util.json_tools as jt
import util.projects_functions as project_funcs
import util.update_check_temp as update_check
import util.support as support
import util.repos as repos
import util.system_stats as system_stats
import util.app_item as app_item
import util.installation_status as installation_status

sg.set_options(
    # button_color=('white', 'green'),
    # button_color=(color.LIGHT_GRAY, color.GRAY),
    # element_size=(50, 20),
    # auto_size_buttons=True,
    # font=('Helvetica', 14),
    # background_color='lightgray',
    # text_color='black',
    sbar_width=15,sbar_trough_color=0,sbar_arrow_width=8,    
    suppress_error_popups = True,
)
__version__ = '0.0.5'
APP_TITLE = f"Super Easy AI Installer Tool - Ver {__version__}"
sg.theme('Dark Gray 15')
python_ver = depcheck.check_python()
git_ver = depcheck.check_git()
usePreInstalledPython=True
project_args = {
    1: ['--autolaunch', '--theme=dark'],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
}

def isfile_exist_check(file_path):
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

def update_project_args(project_id, arg_name):
    if project_id not in project_args:
        project_args[project_id] = []

    if arg_name in project_args[project_id]:
        project_args[project_id].remove(arg_name)
    else:
        project_args[project_id].append(arg_name)

def update_app_args_from_string(app_id, values_string):
    args_list = values_string.split()
    for arg_name in args_list:
        if arg_name not in project_args.get(app_id, []):
            update_project_args(app_id, arg_name)

def get_app_by_id(apps, app_id):
    for app in apps:
        if app.get("id") == app_id:
            return app
    return None

def get_project_id(event):
    return int(re.search(r"_\d+", event).group(0)[1:])

def get_func_and_id(event):
    id_number = get_project_id(event)
    method = re.search(r"-selected_app_func_\d+_(.+)_btn-", event).group(1)
    return id_number,method

def main():
    stop_event = threading.Event()
    nav_tab_mouseover_colors=(color.DARK_GRAY,color.DIM_BLUE)
    nav_tab_button_color=(color.DIM_BLUE,color.DARK_GRAY)
    nav_tab_button_active_color=(color.DARK_GRAY,color.DIM_BLUE)
    is_def =True
    
    #region layout
    top_row = [
        [
            sg.Frame('',[       
                    [
                        sg.Button("Projects",k=PROJECTS_TAB_KEY,disabled=False,font=FONT,expand_x=True,size=(15,2),button_color=nav_tab_button_active_color,mouseover_colors=nav_tab_mouseover_colors),
                        sg.Button("System Monitor",disabled=False,k=SYSTEM_STATS_TAB_KEY,font=FONT,expand_x=True,size=(20,2),button_color=nav_tab_button_color,mouseover_colors=nav_tab_mouseover_colors),
                        sg.Button("AiPanic",disabled=True,k=AIPANIC_TAB_KEY,font=FONT,expand_x=True,size=(10,2),button_color=nav_tab_button_color,mouseover_colors=nav_tab_mouseover_colors),
                        sg.Button("Settings",disabled=True,k=SETTINGS_TAB_KEY,font=FONT,expand_x=True,size=(10,2),button_color=nav_tab_button_color,mouseover_colors=nav_tab_mouseover_colors),
                        sg.Button("About",k=ABOUT_TAB_KEY,font=FONT,expand_x=False,size=(10,2),button_color=nav_tab_button_color,mouseover_colors=nav_tab_mouseover_colors),
                        sg.Button("EN",disabled=True,k=LANGUAGE_TAB_KEY,font=FONT,expand_x=False,size=(5,2),button_color=nav_tab_button_color,mouseover_colors=nav_tab_mouseover_colors),
                    ],                   
            ],expand_x=True,expand_y=False,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.GRAY_9900)        
        ]
    ]
    
    bottom_row = [
        [
            sg.Frame('',[       
                    [
                        # cpbar.progress_bar_custom_layout(PBAR_KEY,visible=True,it_name="file")
                    ],
            ],expand_x=True,border_width=0,relief=sg.RELIEF_FLAT,element_justification='c')
        ],    
    ]

    projects_tab_requirements_column = [
        
        #seait
        [
            sg.Frame('',[       
                [
                    sg.Button(f"Installed version: {__version__}",k=UPDATE_AVAILABLE_LBL_KEY,font=FONT,expand_x=True,size=(30,2),disabled=True),
                ],                
                [
                    sg.Button("Check for update",k=UPDATE_BTN_KEY,font=FONT,expand_x=True,size=(20,1),mouseover_colors=(color.GRAY_9900,color.DIM_BLUE),button_color=(color.DIM_BLUE,None)),
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
                    sg.Button(git_ver ,k=DEP_APP_GIT_INSTALLED_VERSION_LBL_KEY,font=FONT,expand_x=True,size=(40,2),disabled=True),
                ],                
                [
                            sg.Button("Install",k=DEP_APP_GIT_INSTALL_KEY,font=FONT,expand_x=True,size=(10,1),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                ],                                          
            ],expand_x=True,expand_y=False,key=DEP_APP_GIT_INSTALLED_VERSION_FRAME_KEY,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
        ],                              

    ]

    projects_tab_launcher_column = [
        [
            sg.Frame('', [ 
                [
                    sg.Frame('', [
                        [
                            sg.Image(app["image_path"], background_color=color.DARK_GRAY),
                            sg.Button(app["title"], k=f"-select_app_{app['id']}_btn-", font=FONT, expand_x=True, size=(35, 1),button_color=(color.DIM_BLUE,color.GRAY)),
                            sg.Button('', k=f"-select_app_{app['id']}_btn-",font=FONT,disabled=True, expand_x=True,button_color=color.DIM_GREEN if installation_status.check_project(app) else color.GRAY)

                        ],
                    ],
                    expand_x=True,
                    expand_y=False,
                    border_width=5,
                    pad=(3, 3),
                    relief=sg.RELIEF_FLAT,
                    element_justification="l",
                    background_color=color.DARK_GRAY)
                ],
            ],
            expand_x=True,
            expand_y=False,
            border_width=0,
            relief=sg.RELIEF_FLAT,
            element_justification="l",
            background_color=color.DARK_GRAY)
        ]
        for app in projects if app['type'] #== "app" #vertical
    ]
   
    projects_tab_launcher_tab_column_scrollable = [
        # [
        #     sg.Button("SD",k=f"-app_install_tab_installed_github_lbl_key-",font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN),disabled=False),
        #     sg.Button("LLM",k=f"-app_install_tab_installed_github_lbl_key-",font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN),disabled=False),
        #     sg.Button("Other",k=f"-app_install_tab_installed_github_lbl_key-",font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN),disabled=False),
        # ],
        [
            sg.Column(projects_tab_launcher_column, key=C1_LAUNCH_KEY, element_justification='l', expand_x=True,expand_y=True,visible=True,scrollable=True,vertical_scroll_only=True),
        ],
    ] 
      
    system_stats_tab_column = [
        [
            sg.Frame('',[ 
                [
                    sg.Frame('',[ 
         
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

    launcher_column_right_placeholder = [[
        sg.Frame('',[   
            [
                # sg.Button("Select a app to launch",expand_x=True,visible=True,k=f"-selected_app_lbl-",font=FONT,disabled=True)
                sg.Column(projects_tab_requirements_column, key=C2_LAUNCH_PLACE_KEY, element_justification='r', expand_x=True,expand_y=True,visible=True),

            ],
        ],expand_x=True,expand_y=True,border_width=0,pad=(0,0),size=(650,None),relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.DARK_GRAY)
    ]]

    layout = [[ 
            [
                top_row, 
            ],
            [
                sg.Column(projects_tab_launcher_tab_column_scrollable, key=LAUNCH_COLUMN_LEFT_SCROLLABLE_KEY, element_justification='l', expand_x=True,expand_y=True,visible=True),
                sg.Column(launcher_column_right_placeholder, key=C2_LAUNCH_KEY, element_justification='r', expand_x=True,expand_y=True,visible=True),
                sg.Column(about_tab_column, key=C1_ABOUT_KEY, element_justification='c', expand_x=True,expand_y=True,visible=False),
                sg.Column(system_stats_tab_column, key=C1_SYSTEM_STATS_KEY, element_justification='c', expand_x=True,expand_y=True,visible=False),
            ],        
            [
                bottom_row,
            ],
    ]]

    #endregion layout

    window = sg.Window(APP_TITLE,layout,finalize=True,size=(1100,800), resizable=True,enable_close_attempted_event=False,background_color=color.GRAY_9900)
    # window.Maximize()    
    # window.set_min_size((800,600))
    # window.set_min_size((500,300))

    #region nav
    c2_launch_col_scroll:sg.Column = window[LAUNCH_COLUMN_LEFT_SCROLLABLE_KEY]
    c2_launcher_col:sg.Column = window[C2_LAUNCH_KEY]
    c1_about_col:sg.Column = window[C1_ABOUT_KEY]
    c1_system_stats_col:sg.Column = window[C1_SYSTEM_STATS_KEY]
    c1_launcher_widget:sg.Column = window[C1_LAUNCH_KEY].widget
    launcher_tab_btn_elem:sg.Button = window[PROJECTS_TAB_KEY]
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
        PROJECTS_TAB_KEY: [c2_launch_col_scroll,c2_launcher_col],
        ABOUT_TAB_KEY: [c1_about_col],
        SYSTEM_STATS_TAB_KEY: [c1_system_stats_col]
    }

    tab_btn_elements = {
        PROJECTS_TAB_KEY: launcher_tab_btn_elem,
        ABOUT_TAB_KEY: about_tab_btn_elem,
        SYSTEM_STATS_TAB_KEY: system_stats_tab_btn_elem
    }

    active_color = (color.DARK_GRAY, color.DIM_BLUE)
    inactive_color = (color.DIM_BLUE, color.DARK_GRAY)

    expand_column_helper(c1_launcher_widget)
    flatten_ui_elements(window)

    #endregion nav

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
            install_git_btn_elem.update("Installed",disabled_button_color=(color.DIM_GREEN,color.DARK_GREEN),disabled=True)   
        else:
            install_git_btn_elem.update("Install",disabled=False)
            installed_git_version_lbl_elem.update(disabled_button_color=(color.GRAY,color.GRAY),button_color=(color.RED_ORANGE,color.RED_ORANGE),disabled=True)

    def python_event_handler():
        if depcheck.check_python():
            install_python_btn_elem.update("Installed",disabled_button_color=(color.DIM_GREEN,color.DARK_GREEN),disabled=True)   
        else:
            install_python_btn_elem.update("Install",disabled=False)
            installed_version_python_lbl_elem.update(disabled_button_color=(color.GRAY,color.GRAY),button_color=(color.RED_ORANGE,color.RED_ORANGE),disabled=True)
            if is_folder_exist_check(project_funcs.pre_installed_python_path):
                project_funcs.usePreInstalledPython = not project_funcs.usePreInstalledPython
                convert_button_enable() if project_funcs.usePreInstalledPython else convert_button_disable()

        if is_folder_exist_check(project_funcs.pre_installed_python_path):
            # print("pre installed python found")
            project_funcs.usePreInstalledPython = not project_funcs.usePreInstalledPython
            convert_button_enable() if project_funcs.usePreInstalledPython else convert_button_disable()
        else:
            # print("pre installed python not found")         
            pre_installed_version_lbl_elem.update("Pre installed")
            use_python_pre_install_btn_elem.update(disabled_button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True)

    def change_btn_state(x,staus):
        for widget_key,v in window.key_dict.items():
            if str(widget_key).startswith(x):
                window[widget_key].update(disabled=staus) 

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

    def default_launcher_buttons():
        window["-selected_app_args_1_--autolaunch_btn-"].update(button_color=(color.GRAY,color.DIM_GREEN))
        window["-selected_app_args_1_--theme=dark_btn-"].update(button_color=(color.GRAY,color.DIM_GREEN))

    def handle_tab_event(event, tab_elements, tab_btn_elements, active_color, inactive_color):
        if event == "-system_stats_tab-":
            stop_event.clear()
            t = threading.Thread(target=system_stats_monitor, args=(stop_event,2,))
            t.start()
        else:
            stop_event.set()

        for tab_key in tab_elements:
            is_target = tab_key == event
            for element in tab_elements[tab_key]:
                element.update(visible=is_target)
            tab_btn_elements[tab_key].update(button_color=(active_color if is_target else inactive_color))

    def run_project_func(project,method,args=None):

        project_funcs.methods[method](project,args)
        # print(f"running {method} for {project['repo_name']}")

        # window.write_event_value("-run_app_func-",event)    
        window.write_event_value(f"-select_app_{project['id']}_btn-","")    

    git_event_handler()

    python_event_handler() 
         
    for project in projects:
        installation_status.check_project(project)

    while True:
        event, values = window.read()
        # print("event", event)
        if event == sg.WIN_CLOSED:
            break

        if event == DEP_APP_PYTHON_USE_PRE_INSTALL_KEY:
            project_funcs.usePreInstalledPython = not project_funcs.usePreInstalledPython
            convert_button_enable() if project_funcs.usePreInstalledPython else convert_button_disable()

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
   
        if event.startswith(SELECT_APP) and event.endswith("_btn-"):

            id_number = get_project_id(event)

            # window[f"-select_app_{id_number}_btn-"].update(disabled=True,button_color=(color.DARK_GRAY,color.DIM_GREEN))
            # if window[event].ButtonColor[0] == color.GRAY:
            #     window[event].update(button_color=(color.DIM_BLUE,color.GRAY),disabled=False)
            # else:
            #     window[event].update(button_color=(color.GRAY,color.DIM_GREEN),disabled_button_color=(color.GRAY,color.GRAY),disabled=True)            
            # print("triggered",id_number)

            clear_items_keys(window)        
            # fix white flash
            new_layout = app_item.layout(get_app_by_id(projects, id_number))
            for element in list(window[C2_LAUNCH_KEY].Widget.children.values()):
                element.destroy()
            window.extend_layout(window[C2_LAUNCH_KEY],new_layout)
            flatten_ui_elements(window)  
            window.visibility_changed()           
            if id_number == 1:
                default_launcher_buttons() 
                    
        if event.startswith(SELECTED_APP) and event.endswith("_btn-"):
                # print("selected_app_",event)

                if event.startswith("-selected_app_args"):
                    # print("args",event)
                    window.write_event_value(SET_APP_ARGS,event)    

                if event.startswith("-selected_app_func"):
                    # print("func",event)
                    window.write_event_value(RUN_APP_FUNC,event)    

        if event == RUN_APP_FUNC:
            event_value = values['-run_app_func-']
            id_number, method = get_func_and_id(event_value)   
            project = get_app_by_id(projects, id_number)
            if project['type'] == 'app':
                args_list = values[f"-selected_app_args_{id_number}_console_ml-"]
                update_app_args_from_string(id_number, args_list)

            if dialog_window(project['title'],method):
                if method == "install":
                    window[f"-selected_app_func_{id_number}_{method}_btn-"].update("Installing and launching",disabled_button_color=(color.DIM_GREEN,color.GRAY),disabled=True)
                    Thread(target=run_project_func, args=(project,method,project_args[id_number],), daemon=True).start() 
                elif method == "launch":
                    Thread(target=run_project_func, args=(project,method,project_args[id_number],), daemon=True).start() 
                    window[f"-selected_app_func_{id_number}_{method}_btn-"].update("Launched",button_color=(color.GRAY_9900,color.DIM_GREEN),disabled_button_color=(color.GRAY_9900,color.DIM_GREEN),disabled=True)                  
                else:
                    run_project_func(project,method)
   
        if event == SET_APP_ARGS:
            # print("args",event,values['-set_app_args-'])
            event_value = values['-set_app_args-']
            id_number = get_project_id(event_value)
            args = re.search(r"-selected_app_args_\d+_(.+)_btn-", event_value).group(1)   
            update_project_args(id_number,args)
            # print(project_args)
            if window[event_value].ButtonColor[0] == color.GRAY:
                window[event_value].update(button_color=(color.DIM_GREEN,color.GRAY))
            else:
                window[event_value].update(button_color=(color.GRAY,color.DIM_GREEN))

        if event == UPDATE_BTN_KEY:
            if not update_check.check_update_available(__version__).startswith("No update available"):
                update_available_lbl_elem.update(update_check.check_update_available(__version__),button_color=(color.GRAY_9900,color.DARK_GREEN),disabled=False)
            else:
                update_available_lbl_elem.update(update_check.check_update_available(__version__))

        if event == UPDATE_AVAILABLE_LBL_KEY:
            webbrowser.open(LATEST_RELEASE_URL)  
     
        if event.startswith("-selected_app_") and event.endswith("_github_btn-"):
            id_number = get_project_id(event)
            webbrowser.open(get_app_by_id(projects, id_number)['github_url']) 

        support.buttons(event)

        repos.buttons(event)

        # if event == "-start_monitor-":
        #     Thread(target=system_stats_monitor, args=(), daemon=True).start() 

if __name__ == '__main__':

    main() 
