import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *
import util.colors as color
import util.icons as ic
import util.installation_status as installation_status
from util.ui_tools import flatten_ui_elements,expand_column_helper,clear_items_keys
import layout.requirements as requirements_layout 


def create_layout_list_menu(projects):

    layout = [
        # [
        #     sg.Button("SD",k=f"-app_install_tab_installed_github_lbl_key-",font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN),disabled=False),
        #     sg.Button("LLM",k=f"-app_install_tab_installed_github_lbl_key-",font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN),disabled=False),
        #     sg.Button("Other",k=f"-app_install_tab_installed_github_lbl_key-",font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN),disabled=False),
        # ],
        [
            sg.Column(
                [
                        [
                            sg.Frame('', [ 
                                [
                                    sg.Frame('', [
                                        [
                                            sg.Image(project["image_path"], background_color=color.DARK_GRAY),
                                            sg.Button(project["title"], k=f"-select_app_{project['id']}_btn-", font=FONT, expand_x=True, size=(35, 1),button_color=(color.DIM_BLUE,color.GRAY)),
                                            sg.Button('', k=f"-select_app_{project['id']}_btn-",size=(1,1),font=FONT,disabled=True, expand_x=False,button_color=color.DIM_GREEN if installation_status.check_project(project) else color.GRAY)

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
                        for project in projects if project['type'] #== "app" #vertical
                    ]        
        , key=PROJECTS_LIST_MENU, element_justification='l', expand_x=True,expand_y=True,visible=True,scrollable=True,vertical_scroll_only=True),
        ],
    ] 
    return layout


def create_project_layout(lang_data):

    layout = [[
        sg.Frame('',[   
            [
                # sg.Button("Select a app to launch",expand_x=True,visible=True,k=f"-selected_app_lbl-",font=FONT,disabled=True)
                sg.Column(requirements_layout.create_layout(lang_data), key=PROJECTS_COL_PLACEHOLDER, element_justification='r', expand_x=True,expand_y=True,visible=True),
            ],
        ],expand_x=True,expand_y=True,border_width=0,pad=(0,0),size=(650,None),relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.DARK_GRAY)
    ]]

    return layout
# def default_launcher_buttons(project_args, id_number):
#     try:
#         if id_number in project_args:
#             args = project_args[id_number]
#             for arg in args:
#                 button_id = f"-selected_app_args_{id_number}_{arg}_btn-"
#                 window[button_id].update(button_color=(color.GRAY,color.DIM_GREEN))
#     except TypeError as e:
#         print(e)

# def events(window,event,lang_data):
#     if event.startswith(SELECT_APP) and event.endswith("_btn-"):
#         id_number = get_project_id(event)

#         #project_menu_item_highlight
#         # window[f"-select_app_{id_number}_btn-"].update(disabled=True,button_color=(color.DARK_GRAY,color.DIM_GREEN))
#         # if window[event].ButtonColor[0] == color.GRAY:
#         #     window[event].update(button_color=(color.DIM_BLUE,color.GRAY),disabled=False)
#         # else:
#         #     window[event].update(button_color=(color.GRAY,color.DIM_GREEN),disabled_button_color=(color.GRAY,color.GRAY),disabled=True)            
#         # print("triggered",id_number)

#         clear_items_keys(window)        
#         # fix white flash
#         layout = project_layout.layout(get_project_by_id(projects, id_number))
#         for element in list(window[PROJECTS_COL_2].Widget.children.values()):
#             element.destroy()
#         window.extend_layout(window[PROJECTS_COL_2],layout)
#         flatten_ui_elements(window)  
#         window.visibility_changed()           
#         # if id_number == 1:
#         default_launcher_buttons(project_args,id_number) 