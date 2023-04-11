import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *    
import util.icons as ic
import util.dependency_check as depcheck
import util.projects_functions as project_funcs
import os
import subprocess

python_ver = depcheck.check_python()
git_ver = depcheck.check_git()
usePreInstalledPython=True

def create_layout(lang_data):
    Installed_version_local = lang_data["Installed Version"]
    Check_for_update_local = lang_data["Check for Update"]

    layout = [
            
            #seait
            [
                sg.Frame('',[       
                    [
                        sg.Button(f"{Installed_version_local}: {VERSION}",k=UPDATE_AVAILABLE_LBL_KEY,font=FONT,expand_x=True,size=(40,2),disabled=True),
                    ],                
                    [
                        sg.Button(Check_for_update_local,k=CHECK_UPDATE_BTN_KEY,font=FONT,expand_x=True,size=(20,1),mouseover_colors=(color.GRAY_9900,color.DIM_BLUE),button_color=(color.DIM_BLUE,None)),
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
                        sg.Button("Pre Installed - 3.10.6",visible=False,key=PRE_INSTALLED_VERSION_LBL,font=FONT,expand_x=True,size=(20,2),disabled=True),
                        sg.Button(f"{python_ver}",k=INSTALLED_PYTHON_VERSION_LBL,font=FONT,expand_x=True,size=(30,2),disabled=True),
                    ],               
                    [
                        sg.Button("Use pre installed",visible=False,k=USE_PRE_INSTALLED_VERSION_BTN,font=FONT,expand_x=True,size=(20,1),button_color=(color.LIGHT_BLUE,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                        sg.Button("",k=INSTALL_PYTHON_BUTTON,font=FONT,expand_x=True,size=(30,1),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
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
                        sg.Button(git_ver ,k=INSTALLED_GIT_VERSION_LBL,font=FONT,expand_x=True,size=(40,2),disabled=True),
                    ],                
                    [
                                sg.Button("",k=INSTALL_GIT_BUTTON,font=FONT,expand_x=True,size=(20,1),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN)),
                    ],                                          
                ],expand_x=True,expand_y=False,key=DEP_APP_GIT_INSTALLED_VERSION_FRAME_KEY,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
            ],                              
        ]
    return layout

def set_language(window, lang_data):
    window[UPDATE_AVAILABLE_LBL_KEY].update(lang_data["Installed Version"])
    window[CHECK_UPDATE_BTN_KEY].update(lang_data["Check for Update"])
    window[INSTALL_PYTHON_BUTTON].update(lang_data["Check for Update"])
    python_event_handler(window,lang_data)
    git_event_handler(window,lang_data)

def git_event_handler(window,lang_data):
    install = lang_data["Install"]
    installed = lang_data["Installed"]


    if depcheck.check_git():
        window[INSTALL_GIT_BUTTON].update(installed,disabled_button_color=(color.DIM_GREEN,color.DARK_GREEN),disabled=True)   
    else:
        window[INSTALL_GIT_BUTTON].update(install,disabled=False)
        window[INSTALLED_GIT_VERSION_LBL].update(disabled_button_color=(color.GRAY,color.GRAY),button_color=(color.RED_ORANGE,color.RED_ORANGE),disabled=True)

def python_event_handler(window,lang_data):

    installed = lang_data["Installed"]
    install = lang_data["Install"]



    if depcheck.check_python():
        window[INSTALL_PYTHON_BUTTON].update(installed,disabled_button_color=(color.DIM_GREEN,color.DARK_GREEN),disabled=True)   
    else:
        window[INSTALL_PYTHON_BUTTON].update(install,disabled=False)
        window[INSTALLED_PYTHON_VERSION_LBL].update(disabled_button_color=(color.GRAY,color.GRAY),button_color=(color.RED_ORANGE,color.RED_ORANGE),disabled=True)
        if is_folder_exist_check(project_funcs.pre_installed_python_path):
            project_funcs.usePreInstalledPython = not project_funcs.usePreInstalledPython
            convert_button_enable() if project_funcs.usePreInstalledPython else convert_button_disable()

    if is_folder_exist_check(project_funcs.pre_installed_python_path):
        # print("pre installed python found")
        project_funcs.usePreInstalledPython = not project_funcs.usePreInstalledPython
        convert_button_enable() if project_funcs.usePreInstalledPython else convert_button_disable()
    else:
        # print("pre installed python not found")         
        window[PRE_INSTALLED_VERSION_LBL].update("Pre installed")
        window[USE_PRE_INSTALLED_VERSION_BTN].update(disabled_button_color=(color.LIGHT_GRAY,color.GRAY),disabled=True)

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

def convert_button_disable(window):
    window[USE_PRE_INSTALLED_VERSION_BTN].update(button_color=(color.LIGHT_BLUE,color.GRAY))

def convert_button_enable(window):
    window[USE_PRE_INSTALLED_VERSION_BTN].update(button_color=(color.GRAY_9900,color.DARK_GREEN))

def events(window,event,lang_data):
    if event == USE_PRE_INSTALLED_VERSION_BTN:
        project_funcs.usePreInstalledPython = not project_funcs.usePreInstalledPython
        convert_button_enable() if project_funcs.usePreInstalledPython else convert_button_disable()

    if event == INSTALL_PYTHON_BUTTON:
        if isfile_exist_check(INSTALLERS_PYTHON_PATH):
            subprocess.run([INSTALLERS_PYTHON_PATH]) 
            window[INSTALLED_PYTHON_VERSION_LBL].update(python_ver)
            python_event_handler()
        else:
            window[INSTALLED_PYTHON_VERSION_LBL].update("Download the installers version")

    if event == INSTALL_GIT_BUTTON:
        if isfile_exist_check(INSTALLERS_GIT_PATH):
            subprocess.run([INSTALLERS_GIT_PATH])
            window[INSTALLED_GIT_VERSION_LBL].update(git_ver)
            git_event_handler(window,lang_data)
        else:
            window[INSTALLED_GIT_VERSION_LBL].update("Download the installers version")