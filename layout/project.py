import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *
import util.colors as color
import util.icons as ic
import util.installation_status as installation_status

def create_layout(project,lang_data):
    main_key = '-selected_app_'
    selected_app_key = f"{main_key}{project['id']}_"
    installation_status_val = installation_status.check_project(project)
    git_Python_status = installation_status.check_git_python()
    app_commit_hash = installation_status.get_last_commit_hash_local(project)
    
    if app_commit_hash == None:
        app_commit_hash = lang_data["None"]

    launch_buttons_index = 0 if installation_status_val else 1
    launch_buttons_key = f"{main_key}func_{project['id']}_{project['launch_buttons'][launch_buttons_index]['key']}_btn-"
    launch_buttons_button_text = project['launch_buttons'][launch_buttons_index]['button_text']
    launch_buttons_disabled = not git_Python_status
    launch_buttons_button_color = (color.DIM_GREEN, color.GRAY)
    launch_buttons_mouseover_colors = (color.GRAY_9900, color.DIM_GREEN)

    launch_buttons_button = sg.Button(
        lang_data[launch_buttons_button_text],
        disabled=launch_buttons_disabled,
        button_color=launch_buttons_button_color,
        key=launch_buttons_key,
        font=FONT_H1,
        expand_x=True,
        mouseover_colors=launch_buttons_mouseover_colors
    )

    installed_version = lang_data["Installed Version"]
    arguments = lang_data["Arguments"]
    custom = lang_data["Custom"]
    setup = lang_data["Setup"]

    layout = [
        [
            sg.Frame('',[        
                [
                    sg.Image(project['image_path'],key=f"{main_key}img-",background_color=color.DARK_GRAY),
                    sg.Text(project['title'],key=f"{main_key}name-",font=FONT,background_color=color.DARK_GRAY),
                    sg.Push(background_color=color.DARK_GRAY),
                ],        
                [
                    sg.Button(project['github_url'],k=f"{selected_app_key}github_btn-",font=FONT,expand_x=True,button_color=(color.DIM_BLUE,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DIM_BLUE),disabled=False),
                ],                                         
                [
                    sg.Button(installed_version,k=f"{main_key}_{project['id']}_github_lbl-",visible=True,font=FONT,expand_x=True,size=(20,1),disabled=True),
                    sg.Button(app_commit_hash,visible=True,k=f"-{selected_app_key}commit_hash_lbl-",size=(40,1),font=FONT,expand_x=True,disabled=True)
                ],                        
                [ 
                    launch_buttons_button
                ] 
            ],key=f'{main_key}frame-',expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
        ],  
        [
            sg.Frame("",[       
                [
                    sg.MLine(f"""{project['description'][0]}""",k=f"{main_key}description_{project['id']}_console_ml-",visible=True,text_color=color.DIM_BLUE,border_width=10,sbar_width=20,sbar_trough_color=0,
                            autoscroll=True, auto_refresh=True,expand_x=True,expand_y=True,font=FONT,no_scrollbar=True,disabled=True,size=(100,4)),
                ],                            
                ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
        ] if project['description'] else [],         
        [
            sg.Frame("",[       
                [
                    sg.MLine("""This project has not been fully implemented in the installer. If you do not want to deal with errors, it is recommended to skip this one for now.""",k=f"{main_key}isIncomplete{project['id']}_console_ml-",visible=True,text_color=color.RED_ORANGE,border_width=10,sbar_width=20,sbar_trough_color=0,
                            autoscroll=True, auto_refresh=True,expand_x=True,expand_y=True,font=FONT,no_scrollbar=True,disabled=True,size=(100,3)),
                ],                            
                ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
        ] if project['isIncomplete'] else [], 
        [
            sg.Frame("",[       
                [
                    sg.Frame('',[       
                        [
                            sg.Image(ic.args,key=f"{main_key}args_img-",background_color=color.DARK_GRAY,size=(30,30)),
                            sg.Text(arguments,key=f"{main_key}args_lbl-",text_color=color.LIGHT_GRAY,font=FONT,background_color=color.DARK_GRAY),
                        ],  
                    ],key=f"{main_key}args_header_frame-",expand_x=True,expand_y=False,border_width=0,pad=(10,3),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)            
                ],  
                [
                    sg.Frame('',[  
                        [
                            sg.Button(option["button_text"],disabled=False,size=(24,1),button_color=(color.DIM_GREEN,color.GRAY), key=f"{main_key}args_{project['id']}_{option['button_text']}_btn-", font=FONT, expand_x=True,
                                    mouseover_colors=(color.GRAY_9900,color.DIM_GREEN)) for option in arg
                        ]
                        for arg in project['args']
                    ],key=f"{main_key}args_frame-",expand_x=True,expand_y=False,border_width=5,pad=(10,0),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
                ],                            
                ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
        ] if project['args'] else [],    
        [
            sg.Frame(custom,[       
                [
                    sg.MLine("",k=f"{main_key}args_{project['id']}_console_ml-",visible=True,text_color=color.DIM_GREEN,border_width=10,sbar_width=20,sbar_trough_color=0,
                            autoscroll=True, auto_refresh=True,expand_x=True,expand_y=True,font=FONT,no_scrollbar=True,),
                ]                              
                ],key=f"{main_key}args_console_frame-",title_color=color.LIGHT_GRAY,expand_x=True,expand_y=True,border_width=5,pad=(5,0),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.GRAY_1111)
        ] if project['args'] else [],
        [
            sg.Frame('',[       
            [
                sg.Frame('',[       
                    [
                        sg.Image(ic.args,key=f"{main_key}setup_img-",background_color=color.DARK_GRAY,size=(30,30)),
                        sg.Text(setup,key=f"{main_key}setup_lbl-",text_color=color.LIGHT_GRAY,font=FONT,background_color=color.DARK_GRAY),
                    ],  
                ],key=f"{main_key}setup_header_frame-",expand_x=True,expand_y=False,border_width=0,pad=(10,3),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)            
            ],                
            [
                sg.Frame("",[       
                        [
                            sg.Button(lang_data[button['button_text']],disabled=False, key=f"{main_key}func_{project['id']}_{button['key']}_btn-",font=FONT,expand_x=True,button_color=(color.DIM_BLUE,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DIM_BLUE)) 
                            for button in project['buttons']
                        ]
                        if installation_status_val and git_Python_status else [
                           sg.Button(lang_data[button['button_text']],disabled=True, key=f"{main_key}func_{project['id']}_{button['key']}_btn-",font=FONT,expand_x=True,button_color=(color.DIM_BLUE,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DIM_BLUE)) 
                            for button in project['buttons']
                        ]                              
                ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
            ] 
            ],key=f"{main_key}setup_frame-",expand_x=True,expand_y=False,border_width=0,pad=(10,3),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)            
        ],             
       
    ]
    
    return layout
