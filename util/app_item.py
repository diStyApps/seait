import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *
import util.colors as color
import util.icons as ic
import util.installation_status as installation_status

def layout(app):
    main_key = '-selected_app_'
    selected_app_key = f"{main_key}{app['id']}_"
    installation_status_val = installation_status.check_project(app)
    git_Python_status = installation_status.check_git_python()
    app_commit_hash = installation_status.get_last_commit_hash_local(app)

    launch_buttons_index = 0 if installation_status_val else 1
    launch_buttons_key = f"{main_key}func_{app['id']}_{app['launch_buttons'][launch_buttons_index]['key']}_btn-"
    launch_buttons_button_text = app['launch_buttons'][launch_buttons_index]['button_text']
    launch_buttons_disabled = not git_Python_status
    launch_buttons_button_color = (color.DIM_GREEN, color.GRAY)
    launch_buttons_mouseover_colors = (color.GRAY_9900, color.DIM_GREEN)

    launch_buttons_button = sg.Button(
        launch_buttons_button_text,
        disabled=launch_buttons_disabled,
        button_color=launch_buttons_button_color,
        key=launch_buttons_key,
        font=FONT_H1,
        expand_x=True,
        mouseover_colors=launch_buttons_mouseover_colors
    )

    launcher_column_right = [
        [
            sg.Frame('',[        
                [
                    sg.Image(app['image_path'],key=f"{main_key}img-",background_color=color.DARK_GRAY),
                    sg.Text(app['title'],key=f"{main_key}name-",font=FONT,background_color=color.DARK_GRAY),
                    sg.Push(background_color=color.DARK_GRAY),
                ],        
                [
                    sg.Button(app['github_url'],k=f"{selected_app_key}github_btn-",font=FONT,expand_x=True,button_color=(color.DIM_BLUE,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DIM_BLUE),disabled=False),
                ],                                         
                [
                    sg.Button("Installed Version",k=f"{main_key}github_lbl-",visible=True,font=FONT,expand_x=True,size=(20,1),disabled=True),
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
            sg.Frame("Custom",[       
                [
                    sg.MLine("",k=f"{main_key}args_{app['id']}_console_ml-",visible=True,text_color=color.DIM_GREEN,border_width=10,sbar_width=20,sbar_trough_color=0,
                            autoscroll=True, auto_refresh=True,expand_x=True,expand_y=True,font=FONT,no_scrollbar=True,),
                ]                              
                ],key=f"{main_key}args_console_frame-",title_color=color.LIGHT_GRAY,expand_x=True,expand_y=True,border_width=5,pad=(5,0),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.GRAY_1111)
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
                            sg.Button(button['button_text'],disabled=False, key=f"{main_key}func_{app['id']}_{button['key']}_btn-",font=FONT,expand_x=True,button_color=(color.DIM_BLUE,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DIM_BLUE)) 
                            for button in app['buttons']
                        ]
                        if installation_status_val and git_Python_status else [
                           sg.Button(button['button_text'],disabled=True, key=f"{main_key}func_{app['id']}_{button['key']}_btn-",font=FONT,expand_x=True,button_color=(color.DIM_BLUE,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DIM_BLUE)) 
                            for button in app['buttons']
                        ]                              
                ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
            ] 
            ],key=f"{main_key}setup_frame-",expand_x=True,expand_y=False,border_width=0,pad=(10,3),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)            
        ],             
       
    ]
    
    return launcher_column_right