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
import util.installation_status as installation_status
import util.json_tools as jt
import util.project_util as project_util
# import util.system_stats as system_stats
import util.localizations as localizations
import layout.navigation as navigation_layout
import layout.project as project_layout
import layout.about as about_layout
import layout.requirements as requirements_layout 
import layout.dialog as dialog_layout
import layout.projects as projects_layout


def main():
    jt.create_preferences_init()
    languages = localizations.get_language_by_codes()
    lang_data = localizations.set_language(jt.load_preference(PREF_SELECTED_LANG))


    layout = [[ 
            [
                navigation_layout.create_layout(lang_data,languages)
            ],
            [
                sg.Column(projects_layout.create_layout_list_menu(projects_data), key=PROJECTS_COL_1, element_justification='l', expand_x=True,expand_y=True,visible=True),
                sg.Column(projects_layout.create_project_layout(lang_data), key=PROJECTS_COL_2, element_justification='r', expand_x=True,expand_y=True,visible=True),
                sg.Column(about_layout.create_layout(lang_data), key=ABOUT_COL, element_justification='c', expand_x=True,expand_y=True,visible=False),
                # sg.Column(system_stats_layout, key=SYSTEM_INFO_COL, element_justification='c', expand_x=True,expand_y=True,visible=False),
            ],        
    ]]

    window = sg.Window(APP_TITLE,layout,finalize=True,size=(1100,800), resizable=True,enable_close_attempted_event=False,background_color=color.GRAY_9900,icon=ic.icon3)

    #region nav
    projects_layout_col_1:sg.Column = window[PROJECTS_COL_1]
    projects_layout_col_2:sg.Column = window[PROJECTS_COL_2]
    about_layout_col:sg.Column = window[ABOUT_COL]
    # system_stats_layout_col:sg.Column = window[SYSTEM_INFO_COL]

    projects_tab_btn_elem:sg.Button = window[PROJECTS_TAB_BTN]
    about_tab_btn_elem:sg.Button = window[ABOUT_TAB_BTN]
    # system_stats_tab_btn_elem:sg.Button = window[SYSTEM_STATS_TAB_BTN]
    # settings_tab_btn_elem:sg.Button = window[SETTINGS_TAB_BTN]

    update_available_lbl_elem:sg.Text = window[UPDATE_AVAILABLE_LBL_KEY]

    nav_elements = {
        PROJECTS_TAB_BTN: [projects_layout_col_1,projects_layout_col_2],
        ABOUT_TAB_BTN: [about_layout_col],
        # SYSTEM_STATS_TAB_BTN: [system_stats_layout_col]
    }

    nav_btn_elements = {
        PROJECTS_TAB_BTN: projects_tab_btn_elem,
        ABOUT_TAB_BTN: about_tab_btn_elem,
        # SYSTEM_STATS_TAB_BTN: system_stats_tab_btn_elem
    }

    nav_active_color = (color.DARK_GRAY, color.DIM_BLUE)
    nav_inactive_color = (color.DIM_BLUE, color.DARK_GRAY)

    #ui fixes..
    expand_column_helper(window[PROJECTS_LIST_MENU].widget)
    flatten_ui_elements(window)

    #endregion nav

    def default_launcher_buttons(project_args, id_number):
        try:
            if id_number in project_args:
                args = project_args[id_number]
                for arg in args:
                    button_id = f"-selected_app_args_{id_number}_{arg}_btn-"
                    window[button_id].update(button_color=(color.GRAY,color.DIM_GREEN))
        except TypeError as e:
            print(e)

    def run_project_func(project,method,args=None):
        project_funcs.methods[method](project,args) 
        window.write_event_value(f"-select_app_{project['id']}_btn-","")    

    requirements_layout.git_event_handler(window,lang_data)
    requirements_layout.python_event_handler(window,lang_data) 

    while True:
        event, values = window.read()
        # print("event", event, "values", values)

        if event == sg.WIN_CLOSED:
            break

        requirements_layout.events(window,event,lang_data)
        about_layout.events(event)

        if event == SET_LANGUAGE:
            jt.save_preference(PREF_SELECTED_LANG,localizations.get_language_by_native(values[SET_LANGUAGE]))
            reopen_window(window)

        if event in nav_elements:
            navigation_layout.handle_tab_event(event, nav_elements, nav_btn_elements, nav_active_color, nav_inactive_color)
   
        if event.startswith(SELECT_APP) and event.endswith("_btn-"):
            id_number = project_util.get_project_id(event)

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
            window.extend_layout(window[PROJECTS_COL_2],layout)
            flatten_ui_elements(window)  
            window.visibility_changed()           
            # if id_number == 1:
            default_launcher_buttons(project_args,id_number) 
                    
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
            id_number, method = project_util.get_function_and_project_id(event_value)   
            project = project_util.get_project_by_id(projects_data, id_number)
            if project['type'] == 'app':
                args_list = values[f"-selected_app_args_{id_number}_console_ml-"]
                project_util.update_project_args_from_string(id_number, args_list)

            if dialog_layout.dialog_window(project['title'],method,lang_data):
                if method == "install":
                    Installing_and_launching_local = localizations.set_language_by_native(values[SET_LANGUAGE])["Installing and launching"]                    
                    window[f"-selected_app_func_{id_number}_{method}_btn-"].update(Installing_and_launching_local,disabled_button_color=(color.DIM_GREEN,color.GRAY),disabled=True)
                    Thread(target=run_project_func, args=(project,method,project_args[id_number],), daemon=True).start() 
                elif method == "launch":
                    Launched_local = localizations.set_language_by_native(values[SET_LANGUAGE])["Launched"]                     
                    Thread(target=run_project_func, args=(project,method,project_args[id_number],), daemon=True).start() 
                    window[f"-selected_app_func_{id_number}_{method}_btn-"].update(Launched_local,button_color=(color.GRAY_9900,color.DIM_GREEN),disabled_button_color=(color.GRAY_9900,color.DIM_GREEN),disabled=True)                  
                else:
                    run_project_func(project,method)
   
        if event == SET_APP_ARGS:
            # print("args",event,values['-set_app_args-'])
            event_value = values['-set_app_args-']
            id_number = project_util.get_project_id(event_value)
            args = re.search(r"-selected_app_args_\d+_(.+)_btn-", event_value).group(1)   
            project_util.update_project_args(id_number,args)
            # print(project_args)
            if window[event_value].ButtonColor[0] == color.GRAY:
                window[event_value].update(button_color=(color.DIM_GREEN,color.GRAY))
            else:
                window[event_value].update(button_color=(color.GRAY,color.DIM_GREEN))

        if event == CHECK_UPDATE_BTN_KEY:
            if not update_check.check_update_available():
                update_available = localizations.set_language_by_native(values[SET_LANGUAGE])[LOCAL_UPDATE_AVAILABLE]
                update_available_lbl_elem.update(f"{update_available}: {update_check.latest_release}",button_color=(color.GRAY_9900,color.DARK_GREEN),disabled=False)
            else:
                no_update_available = localizations.set_language_by_native(values[SET_LANGUAGE])[LOCAL_NO_UPDATE_AVAILABLE]
                update_available_lbl_elem.update(f"{no_update_available}: {VERSION}")

        if event == UPDATE_AVAILABLE_LBL_KEY:
            webbrowser.open(LATEST_RELEASE_URL)  
     
        if event.startswith("-selected_app_") and event.endswith("_github_btn-"):
            id_number = project_util.get_project_id(event)
            webbrowser.open(project_util.get_project_by_id(projects_data, id_number)['github_url']) 


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
