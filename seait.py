import PySimpleGUI as sg
import re
from threading import Thread
import webbrowser
from util.CONSTANTS import *
from util.ui_tools import flatten_ui_elements,expand_column_helper,clear_items_keys
import util.colors as color
import util.icons as ic
from util.projects_data import projects_data
import util.projects_functions as project_funcs
import util.update_check_temp as update_check
import util.json_tools as jt
from util.json_tools_projects import get_pref_project_data,add_project,set_project_active,add_project_def_args
from util.util import contains_spaces,convert_list_to_string,convert_string_to_list

import util.project_util as project_util
# import util.system_stats as system_stats
import util.localizations as localizations
import layout.navigation as navigation_layout
import layout.project as project_layout
import layout.about as about_layout
import layout.requirements as requirements_layout 
import layout.dialog as dialog_layout
import layout.projects as projects_layout
import layout.settings as settings_layout
import layout.toolbox as toolbox_layout

import os
def main():
    jt.create_preferences_init()
    languages = localizations.get_language_by_codes()
    lang_data = localizations.set_language(jt.load_preference(PREF_SELECTED_LANG))
    window_width = 1250
    layout = [[ 
            [
                navigation_layout.create_layout(lang_data)
            ],
            [
                sg.Column(projects_layout.create_layout_list_menu(projects_data), key=PROJECTS_COL_1, element_justification='l', expand_x=True,expand_y=True,visible=True),
                sg.Column(projects_layout.create_project_layout(lang_data,projects_data), key=PROJECTS_COL_2, element_justification='r', expand_x=True,expand_y=True,visible=True),
                sg.Column(about_layout.create_layout(lang_data), key=ABOUT_COL, element_justification='c', expand_x=True,expand_y=True,visible=False),
                sg.Column(settings_layout.create_layout(lang_data,languages), key=SETTINGS_COL, element_justification='c', expand_x=True,expand_y=True,visible=False),
                sg.Column(toolbox_layout.create_layout(lang_data,languages), key=TOOLBOX_COL, element_justification='c', expand_x=True,expand_y=True,visible=False),

                # sg.Column(system_stats_layout, key=SYSTEM_INFO_COL, element_justification='c', expand_x=True,expand_y=True,visible=False),
            ],        
    ]]
    window = sg.Window(APP_TITLE,layout,finalize=True,size=(window_width,849),ttk_theme='alt', resizable=True,enable_close_attempted_event=False,background_color=color.GRAY_9900,icon=ic.icon3)
    update_available_lbl_elem:sg.Text = window[UPDATE_AVAILABLE_LBL_KEY]

    #region nav
    projects_layout_col_1:sg.Column = window[PROJECTS_COL_1]
    projects_layout_col_2:sg.Column = window[PROJECTS_COL_2]
    projects_tab_btn_elem:sg.Button = window[PROJECTS_TAB_BTN]

    about_layout_col:sg.Column = window[ABOUT_COL]
    about_tab_btn_elem:sg.Button = window[ABOUT_TAB_BTN]

    settings_layout_col:sg.Column = window[SETTINGS_COL]
    settings_tab_btn_elem:sg.Button = window[SETTINGS_TAB_BTN]
    toolbox_layout_col:sg.Column = window[TOOLBOX_COL]
    toolbox_tab_btn_elm:sg.Button = window[TOOLBOX_TAB_BTN]


    nav_elements = {
        PROJECTS_TAB_BTN: [projects_layout_col_1,projects_layout_col_2],
        ABOUT_TAB_BTN: [about_layout_col],
        SETTINGS_TAB_BTN: [settings_layout_col],
        TOOLBOX_TAB_BTN: [toolbox_layout_col]
    }

    nav_btn_elements = {
        PROJECTS_TAB_BTN: projects_tab_btn_elem,
        ABOUT_TAB_BTN: about_tab_btn_elem,
        SETTINGS_TAB_BTN: settings_tab_btn_elem,
        TOOLBOX_TAB_BTN: toolbox_tab_btn_elm
    }

    nav_active_color = (color.DARK_GRAY, color.DIM_BLUE)
    nav_inactive_color = (color.DIM_BLUE, color.DARK_GRAY)

    #ui fixes..
    expand_column_helper(window[PROJECTS_LIST_MENU].widget)    
    expand_column_helper(window['-hub_scroll-'].widget)    



    
    window.visibility_changed()           
    window[PROJECTS_LIST_MENU].contents_changed()  



    flatten_ui_elements(window)
    window.size = (window_width,850)
    
    #endregion nav

    def run_project_func(project,method,args=None):
        project_funcs.methods[method](project,args) 
        window.write_event_value(f"-select_app_{project['id']}_btn-","")    

    def set_project_path(window, id_number, input_project_path,trigger_event=True):
        if input_project_path:
                add_project(id_number, input_project_path,False) 
                if trigger_event:
                    window.write_event_value(f"-select_app_{id_number}_btn-",'')    

    requirements_layout.git_event_handler(window,lang_data)
    requirements_layout.python_event_handler(window,lang_data) 


    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED:
            break
        print(event)

        if event == SET_LANGUAGE:
            jt.save_preference(PREF_SELECTED_LANG,localizations.get_language_by_native(values[SET_LANGUAGE]))
            reopen_window(window)

        if event in nav_elements:
            navigation_layout.handle_tab_event(event, nav_elements, nav_btn_elements, nav_active_color, nav_inactive_color)
   
        if event.startswith(SELECT_APP) and event.endswith("_btn-"):
            id_number = project_util.get_project_id(event)
            # print("select_app_",event)
            #project_menu_item_highlight
            # window[f"-select_app_{id_number}_btn-"].update(disabled=True,button_color=(color.DARK_GRAY,color.DIM_GREEN))
            # if window[event].ButtonColor[0] == color.GRAY:
            #     window[event].update(button_color=(color.DIM_BLUE,color.GRAY),disabled=False)
            # else:
            #     window[event].update(button_color=(color.GRAY,color.DIM_GREEN),disabled_button_color=(color.GRAY,color.GRAY),disabled=True)            
            # print("triggered",id_number)

            clear_items_keys(window)        
            # fix white flash
            project = project_util.get_project_by_id(projects_data, id_number)
            layout = project_layout.create_layout(project,lang_data)
            
            for element in list(window[PROJECTS_COL_2].Widget.children.values()):
                element.destroy()

            window.write_event_value(INIT_DEFAULT_PROJECT_ARGS,id_number)  
            window.extend_layout(window[PROJECTS_COL_2],layout)

            if project['type'] == "app":
                if project['args']:
                    try:
                        expand_column_helper(window[f"-selected_app_scroll_frame-"].widget)
                    except KeyError:
                        pass
                    except AttributeError:
                        pass

            flatten_ui_elements(window)  
            window.visibility_changed()           
        
        if event == INIT_DEFAULT_PROJECT_ARGS:
                id_number = values[INIT_DEFAULT_PROJECT_ARGS]
                project_pref_def_args = project['def_args']
                input_project_path = values[f'-selected_app_{id_number}_project_path_in-']
                if not contains_spaces(input_project_path):
                    if not get_pref_project_data(id_number):
                        set_project_path(window, id_number, input_project_path,False)
                        add_project_def_args(id_number, convert_list_to_string(project_pref_def_args))
                        window.write_event_value(f"-select_app_{id_number}_btn-",'')    
                else:
                    print(f"Path cannot contain spaces. {input_project_path}")

        if event.startswith(SELECTED_APP) and event.endswith("_btn-"):

                if event.startswith("-selected_app_args"):
                    window.write_event_value(SET_APP_ARGS,event)    
                if event.startswith("-selected_app_func"):
                    window.write_event_value(RUN_APP_FUNC,event)   
                if event.startswith("-selected_app_quick"):
                    window.write_event_value(SELECTED_APP_QUICK,event)    
                if event.endswith("_project_path_set_btn-"):
                    window.write_event_value(SET_PROJECT_PATH,id_number)    
                if event.endswith("_project_path_activate_btn-"):
                    window.write_event_value(ACTIVATE_PROJECT_PATH,id_number) 
                if event.endswith("_project_path_add_folder_name_btn-"):
                    window.write_event_value(ADD_PROJECT_FOLDER_NAME,id_number) 
                if event.endswith("_project_save_def_args_btn-"):
                    window.write_event_value(SAVE_DEFAULT_ARGS,id_number)   

        if event == RUN_APP_FUNC:
            event_value = values['-run_app_func-']
            id_number, method = project_util.get_function_and_project_id(event_value)   
            project = project_util.get_project_by_id(projects_data, id_number)
            arguments = ""
            if project['type'] == 'app':
                if project['args']:
                    arguments = convert_string_to_list(values[f"-selected_app_args_{id_number}_console_ml-"])

            if dialog_layout.dialog_window(project['title'],method,lang_data):
                if method == "install":
                    Installing_and_launching_local = localizations.set_language_by_native(values[SET_LANGUAGE])["Installing and launching"]                    
                    window[f"-selected_app_func_{id_number}_{method}_btn-"].update(Installing_and_launching_local,disabled_button_color=(color.DIM_GREEN,color.GRAY),disabled=True)
                    Thread(target=run_project_func, args=(project,method,arguments,), daemon=True).start() 
                elif method == "launch":
                    Launched_local = localizations.set_language_by_native(values[SET_LANGUAGE])["Launched"]                     
                    Thread(target=run_project_func, args=(project,method,arguments,), daemon=True).start() 
                    window[f"-selected_app_func_{id_number}_{method}_btn-"].update(Launched_local,button_color=(color.GRAY_9900,color.DIM_GREEN),disabled_button_color=(color.GRAY_9900,color.DIM_GREEN),disabled=True)                  
                else:
                    run_project_func(project,method)
   

        if event == SELECTED_APP_QUICK:
            event_value = values[SELECTED_APP_QUICK]
            id_number, method = project_util.get_function_and_project_id_quick_launch(event_value)   
            project = project_util.get_project_by_id(projects_data, id_number)
            arguments = ""
            if project['type'] == 'app':
                if project['args']:
                    # arguments = convert_string_to_list(values[f"-selected_app_args_{id_number}_console_ml-"])
                    # if not values[f"-selected_app_args_{id_number}_console_ml-"]:
                        arguments = convert_string_to_list(get_pref_project_data(id_number)['def_args'])
            Launched_local = localizations.set_language_by_native(values[SET_LANGUAGE])["Launched"]                     
            Thread(target=run_project_func, args=(project,method,arguments,), daemon=True).start() 
            window[f"-selected_app_quick_{id_number}_{method}_btn-"].update(Launched_local,button_color=(color.GRAY_9900,color.DIM_GREEN),disabled_button_color=(color.GRAY_9900,color.DIM_GREEN),disabled=True)                  


        if event == SET_APP_ARGS:
            event_value = values['-set_app_args-']
            id_number = project_util.get_project_id(event_value)
            args = re.search(r"-selected_app_args_\d+_(.+)_btn-", event_value).group(1)
            args_console_multiline = values[f"-selected_app_args_{id_number}_console_ml-"]

            if window[event_value].ButtonColor[0] == color.GRAY:
                window[event_value].update(button_color=(color.DIM_BLUE, color.GRAY))
                updated_args = args_console_multiline.replace(args, "").strip()
                window[f"-selected_app_args_{id_number}_console_ml-"].update(updated_args)
            else:
                window[event_value].update(button_color=(color.GRAY, color.DIM_GREEN))
                window[f"-selected_app_args_{id_number}_console_ml-"].update(f"{args_console_multiline} {args}")

        if event == ACTIVATE_PROJECT_PATH:
            id_number = values[ACTIVATE_PROJECT_PATH]
            input_project_path = values[f'-selected_app_{id_number}_project_path_in-']
            if input_project_path:
                project_pref = get_pref_project_data(id_number)
                if project_pref:
                    project_pref_isSet = project_pref['isSet']
                    if project_pref_isSet:
                        set_project_active(id_number, False)
                    else:
                        set_project_active(id_number, True)
            window.write_event_value(f"-select_app_{id_number}_btn-",'')    

        if event == ADD_PROJECT_FOLDER_NAME:
            id_number = values[ADD_PROJECT_FOLDER_NAME]
            input_project_path = values[f'-selected_app_{id_number}_project_path_in-']
            project = project_util.get_project_by_id(projects_data, id_number)
            project_name = project['repo_name']

            if not input_project_path.endswith(project_name):
                window[f'-selected_app_{id_number}_project_path_in-'].update(f"{input_project_path}/{project_name}")
            else:
                print("Can only add project folder to path if it is not already in the path, you can add it manually if you want to.")

        if event == SET_PROJECT_PATH:
            id_number = values[SET_PROJECT_PATH]
            input_project_path = values[f'-selected_app_{id_number}_project_path_in-']
            if not contains_spaces(input_project_path):
                set_project_path(window, id_number, input_project_path)
            else:
                print(f"Path cannot contain spaces. {input_project_path}")

        if event == SAVE_DEFAULT_ARGS:
            id_number = values[SAVE_DEFAULT_ARGS]
            args = values[f"-selected_app_args_{id_number}_console_ml-"]
            input_project_path = values[f'-selected_app_{id_number}_project_path_in-']
            if not contains_spaces(input_project_path):
                set_project_path(window, id_number, input_project_path,False)
                add_project_def_args(id_number, args)
                window.write_event_value(f"-select_app_{id_number}_btn-",'')    
            else:
                print(f"Path cannot contain spaces. {input_project_path}")




        if event == CHECK_UPDATE_BTN_KEY:
            latest_release = update_check.check_update_available()
            if latest_release:
                update_available = localizations.set_language_by_native(values[SET_LANGUAGE])[LOCAL_UPDATE_AVAILABLE]
                update_available_lbl_elem.update(f"{update_available}: {latest_release}",button_color=(color.GRAY_9900,color.DARK_GREEN),disabled=False)
            else:
                no_update_available = localizations.set_language_by_native(values[SET_LANGUAGE])[LOCAL_NO_UPDATE_AVAILABLE]
                update_available_lbl_elem.update(f"{no_update_available}: {VERSION}")

        if event == UPDATE_AVAILABLE_LBL_KEY:
            webbrowser.open(LATEST_RELEASE_URL)  
     
        if event.startswith("-selected_app_") and event.endswith("_github_btn-"):
            id_number = project_util.get_project_id(event)
            webbrowser.open(project_util.get_project_by_id(projects_data, id_number)['github_url']) 
        
        about_layout.events(event)
        toolbox_layout.events(event,values,window)


        
if __name__ == '__main__':
    sg.theme('Dark Gray 15')

    sg.set_options(
        # button_color=('white', 'green'),
        # button_color=(color.LIGHT_GRAY, color.GRAY),
        # element_size=(50, 20),
        # auto_size_buttons=True,
        # font=('Helvetica', 14),
        # background_color='lightgray',
        # text_color='black',
        # ttk_theme='classic',
        sbar_width=15,sbar_trough_color=0,sbar_arrow_width=8,    
        suppress_raise_key_errors=True,
        suppress_error_popups=True,
        suppress_key_guessing=True    
    )

    def suppress_errors(*args, **kwargs):
        pass

    sg.Print = suppress_errors  

    def reopen_window(window):
        window.close()
        main()  

    main() 
