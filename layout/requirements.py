import PySimpleGUI as sg
import util.colors as color
import util.icons as ic
from util.CONSTANTS import *    
from util.util import isfile_exist_check
from util.dependency_check import check_git, detect_python
import subprocess
import layout.quick_launch as quick_launch
import os
python = "Python"
git = "Git"
version = "version"
download_iv = "Please download the installers version"


def create_layout(lang_data,projects):
    # path_spaces = True
    python_ver = detect_python()

    layout = [               
            #seait
            [
                sg.Frame('',[       
                    [
                        sg.Button(f"{lang_data[LOCAL_INSTALLED_VERSION]}: {VERSION}",k=UPDATE_AVAILABLE_LBL_KEY,font=FONT,expand_x=True,size=(40,2),disabled=True),
                    ],                
                    [
                        sg.Button(lang_data[LOCAL_CHECK_FOR_UPDATE],k=CHECK_UPDATE_BTN_KEY,font=FONT,expand_x=True,size=(20,1),mouseover_colors=(color.GRAY_9900,color.DIM_BLUE),button_color=(color.DIM_BLUE,None)),
                    ],                                                          
                ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY,visible=True)
            ], 
            #Python
            [
                sg.Frame('',[       
                            [
                                sg.Image(data=ic.python,background_color=color.DARK_GRAY),
                                sg.Text(python,font=FONT,background_color=color.DARK_GRAY),
                            ],  
                    [
                        sg.Button("",k=INSTALLED_PYTHON_VERSION_LBL,font=FONT,expand_x=True,size=(30,2),disabled=True),
                    ],    
                                      
                    [
                        sg.Button("",k=INSTALL_PYTHON_BUTTON,font=FONT,expand_x=True,size=(30,1),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                    ], 
                                       
                ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY),
                sg.Frame('',[       
                            [
                                sg.Image(data=ic.git,background_color=color.DARK_GRAY),
                                sg.Text(git,font=FONT,background_color=color.DARK_GRAY),
                            ],  
                    [
                     sg.Button('' ,k=INSTALLED_GIT_VERSION_LBL,font=FONT,expand_x=True,size=(40,2),disabled=True),
                    ],  
                              
                    [
                      sg.Button("",k=INSTALL_GIT_BUTTON,font=FONT,expand_x=True,size=(20,1),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                    ],                                          
                ],expand_x=True,expand_y=False,key=DEP_APP_GIT_INSTALLED_VERSION_FRAME_KEY,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY), 
  
            ],   
            [
                sg.Frame('',[       
                    [
                        sg.Button(lang_data[LOCAL_CHECK_PYTHON_PATH],k="LOCAL_CHECK_PYTHON_PATH_LBL",
                                  disabled_button_color=(color.RED_ORANGE,color.DARK_GRAY),
                                  button_color=(color.RED_ORANGE,color.DARK_GRAY),
                                  font=FONT,expand_x=True,size=(60,2),disabled=True,visible=True),
                    ]
                    if not python_ver else [
                        sg.Button(lang_data[LOCAL_CHECK_PYTHON_PATH],k="LOCAL_CHECK_PYTHON_PATH_LBL",
                                        disabled_button_color=(color.RED_ORANGE,color.DARK_GRAY),
                                        button_color=(color.RED_ORANGE,color.DARK_GRAY),
                                        font=FONT,expand_x=True,size=(60,2),disabled=True,visible=True),        
                    ],                                         
                ],expand_x=True,expand_y=False,visible=False,k=LOCAL_CHECK_PYTHON_PATH_LBL,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)        
            ],
            [
                quick_launch.create_layout(lang_data,projects),
            ],

        ]
    return layout

def git_event_handler(window,lang_data):
    git_ver = check_git()
    if git_ver:
        window[INSTALL_GIT_BUTTON].update(lang_data[LOCAL_INSTALLED],disabled_button_color=(color.DIM_GREEN,color.DARK_GREEN),disabled=True)   
        window[INSTALLED_GIT_VERSION_LBL].update(git_ver,disabled_button_color=(color.LIGHT_GRAY,color.LIGHT_GRAY),button_color=(color.GRAY,color.GRAY))

    else:
        window[INSTALL_GIT_BUTTON].update(lang_data[LOCAL_INSTALL],disabled=False)
        window[INSTALLED_GIT_VERSION_LBL].update(lang_data[LOCAL_NONE],disabled_button_color=(color.GRAY,color.GRAY),button_color=(color.RED_ORANGE,color.RED_ORANGE),disabled=True)

def python_event_handler(window,lang_data):
    python_ver = detect_python()
    if python_ver:
        window[INSTALL_PYTHON_BUTTON].update(lang_data[LOCAL_INSTALLED],disabled_button_color=(color.DIM_GREEN,color.DARK_GREEN),disabled=True)   
        window[INSTALLED_PYTHON_VERSION_LBL].update(python_ver[version],disabled_button_color=(color.LIGHT_GRAY,color.LIGHT_GRAY),button_color=(color.GRAY,color.GRAY)) 
        window[LOCAL_CHECK_PYTHON_PATH_LBL].update(visible=False)
    else:
        window[INSTALL_PYTHON_BUTTON].update(lang_data[LOCAL_INSTALL],disabled=False)
        window[INSTALLED_PYTHON_VERSION_LBL].update(lang_data[LOCAL_NONE],disabled_button_color=(color.GRAY,color.GRAY),button_color=(color.RED_ORANGE,color.RED_ORANGE),disabled=True)
        window[LOCAL_CHECK_PYTHON_PATH_LBL].update(visible=True)

def convert_button_disable(window):
    window[USE_PRE_INSTALLED_VERSION_BTN].update(button_color=(color.LIGHT_BLUE,color.GRAY))

def convert_button_enable(window):
    window[USE_PRE_INSTALLED_VERSION_BTN].update(button_color=(color.GRAY_9900,color.DARK_GREEN))

def events(window,event,lang_data):

    if event == INSTALL_PYTHON_BUTTON:
        if isfile_exist_check(INSTALLERS_PYTHON_PATH):
            subprocess.run([INSTALLERS_PYTHON_PATH]) 
            python_event_handler(window,lang_data)
        else:
            window[INSTALLED_PYTHON_VERSION_LBL].update(download_iv)

    if event == INSTALL_GIT_BUTTON:
        if isfile_exist_check(INSTALLERS_GIT_PATH):
            subprocess.run([INSTALLERS_GIT_PATH])
            git_event_handler(window,lang_data)
        else:
            window[INSTALLED_GIT_VERSION_LBL].update(download_iv)