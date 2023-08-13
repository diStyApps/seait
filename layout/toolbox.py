
import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *
import util.icons as ic
import util.json_tools as jt
import util.symlink_creator as symlink
import os
import re
from util.path_handler import full_path

folders={
    "Checkpoints":"checkpoints",
    "Embeddings":"embeddings",
    "Lora":"lora",
    'Dreambooth':"dreambooth",
    'Hypernetworks':"hypernetworks",
    'ControlNet':"controlnet",
    'Codeformer':"codeformer",
    'Deepbooru':"deepbooru", 
    'ModelScope':"modelscope",
    'Openpose':"openpose",
    'BLIP':"blip",
    'ESRGAN':"esrgan",
    'GFPGAN':"gfpgan",
    'LDSR':"ldsr",
    'SwinIR':"swinir",
    "VAE":"vae",
    'VAE-approx':"vae_approx",
    'Diffusers':"diffusers",
    'Language models':"language_models"
}
def convert_to_backslashes(file_path):
    return file_path.replace("\\", "/")



def create_layout(lang_data,tools):
    main_folder = 'models_treasury'
    getcwd = convert_to_backslashes(os.path.abspath(os.getcwd()))
    # path = convert_to_backslashes(os.path.join(getcwd,main_folder))
    path = convert_to_backslashes(os.path.join(full_path,main_folder))

    preference_models_treasury_path =  jt.load_preference('models_treasury_path')
    if not preference_models_treasury_path == None:
        path = preference_models_treasury_path


    tools =[
        "Symlink",
    ]

    col1 = [
        [
            sg.Frame('',[       
                        [
                            sg.Image(data=ic.args,background_color=color.DARK_GRAY),
                            sg.Text(lang_data[LOCAL_TOOLS],font=FONT,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                        ],  
                        [
                            sg.Combo(tools, default_value=tools[0], s=(1, 20), enable_events=True, readonly=True, k=SET_LANGUAGE, expand_x=True, expand_y=False,
                                    font=FONT,text_color=color.DIM_BLUE,button_background_color=color.DARK_GRAY,button_arrow_color=color.DARK_GRAY,disabled=False),                         
                        ],  
                ],expand_x=True,expand_y=False,border_width=5,pad=(5,5),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY),        
        ],
        [
            sg.Frame('',[    
                        [
                            sg.Text(lang_data[LOCAL_WARNING].upper(),font=FONT,text_color=color.RED_ORANGE,background_color=color.DARK_GRAY),
                        ],    
                        [
                            sg.Text(lang_data[LOCAL_CLOSE_RUNNING_PROJECTS],size=(45,2),font=FONT,text_color=color.RED_ORANGE,background_color=color.DARK_GRAY),
                        ],         
                        [
                            sg.ML(f"""
{lang_data[LOCAL_WARNING_SYMLINK_MSG]}
""",
                            font=FONT,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY,size=(10,10),expand_x=True,expand_y=True,visible=True,no_scrollbar=True,disabled=True),
                        ],  
                ],expand_x=True,expand_y=False,border_width=5,pad=(5,5),size=(250,200),relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.DARK_GRAY),        
        ],

    ]

    
    col2 = [
        [
            sg.Frame('',[       
                    [
                        sg.Image(data=ic.args,background_color=color.DARK_GRAY),
                        sg.Text(f"Symlink Creator",font=FONT,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                    ],  
                    [
                        sg.Frame('',[       

                        [
                            sg.Text(lang_data[LOCAL_SOURCE],font=FONT_M_B,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                        ],                                  
                        [
                            sg.In(key=SOURCE_CUSTOM_SYMLINK_PATH_IN,
                                enable_events=True,expand_x=True,expand_y=True,
                                font=FONT,
                                text_color=color.LIGHT_GRAY,  
                                background_color=color.GRAY,  
                                ),
                            sg.FolderBrowse(button_text=lang_data[LOCAL_BROWSE],k=SOURCE_CUSTOM_SYMLINK_PATH_FOLDER_BROWSE,
                                    button_color=(color.DIM_BLUE, color.GRAY),
                                    size=(None,2)    
                                ),                                                  
                        ],  
                        [
                            sg.Text(lang_data[LOCAL_TARGET],font=FONT_M_B,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                        ],                                  
                        [
                            sg.In(key=TARGET_CUSTOM_SYMLINK_PATH_IN,
                                enable_events=True,expand_x=True,expand_y=True,
                                font=FONT,
                                text_color=color.LIGHT_GRAY,  
                                background_color=color.GRAY,  
                                ),
                            sg.FolderBrowse(button_text=lang_data[LOCAL_BROWSE],k=TARGET_CUSTOM_SYMLINK_PATH_FOLDER_BROWSE,
                                button_color=(color.DIM_BLUE, color.GRAY),
                                size=(None,2)),                                                  
                        ],  
                        [
                            sg.Button(
                                    button_text=f'{lang_data[LOCAL_CREATE]} Symlink',
                                    button_color=(color.DIM_BLUE, color.GRAY),
                                    key=CREATE_SYMLINK_BTN, 
                                    expand_x=True, 
                                    expand_y=True, 
                                    mouseover_colors=(color.GRAY_9900, color.DIM_BLUE),
                                    font=FONT_H1,
                                    # size=(50,2)
                                ),        
                        ],            
                        [
                            sg.Frame('',[       

                            [
                                sg.Text(lang_data[LOCAL_REMOVE],font=FONT_M_B,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                                sg.Text(lang_data[LOCAL_REMOVE_SYMLINK_TOOLTIP],font=FONT_S,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                            ],                                  
                            [
                                sg.In(key=REMOVE_SYMLINK_PATH_IN,
                                    enable_events=True,expand_x=True,expand_y=True,
                                    font=FONT,
                                    text_color=color.LIGHT_GRAY,  
                                    background_color=color.GRAY),           
                                sg.Button(
                                                button_text=f'{lang_data[LOCAL_REMOVE]} Symlink',
                                                button_color=(color.DIM_BLUE, color.GRAY),
                                                key=REMOVE_SYMLINK_BTN, 
                                                mouseover_colors=(color.GRAY_9900, color.DIM_BLUE))                                                                    
                            ],  
                                ],expand_x=True,expand_y=False,border_width=0,pad=(0,0),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY),        
                        ],
                            ],expand_x=True,expand_y=False,border_width=5,pad=(5,5),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY),        
                    ],



            ],expand_x=True,expand_y=False,border_width=5,pad=(5,5),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)        
        ],

        [
            sg.Frame('',[       
                    [
                        sg.Image(data=ic.args,background_color=color.DARK_GRAY),
                        sg.Text(lang_data[LOCAL_MODELS_TREASURY],font=FONT,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                      
                    ],  

            ],expand_x=True,expand_y=False,border_width=5,pad=(5,5),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)        
        ],     
        [
            sg.Frame('',[        
                        [
                            sg.Text(f"{lang_data[LOCAL_SET]} {lang_data[LOCAL_MODELS_TREASURY]}",font=FONT_S,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                        ],                                  
                        [
                            sg.In(default_text=path,key=MODEL_TREASURY_PATH_IN,
                                expand_x=True,expand_y=True,
                                font=FONT,
                                text_color=color.LIGHT_GRAY,  
                                background_color=color.GRAY,  
                                ),
                            sg.FolderBrowse(button_text=lang_data[LOCAL_BROWSE],k=MODEL_TREASURY_PATH_FOLDER_BROWSE,
                                    button_color=(color.DIM_BLUE, color.GRAY),
                                    size=(None,2)    
                                ),                  
                            sg.Button(
                                    button_text=lang_data[LOCAL_SET],
                                    button_color=(color.DIM_BLUE, color.GRAY),
                                    key=SET_MODEL_TREASURY_FOLDER_BTN, 
                                    expand_x=False, 
                                    mouseover_colors=(color.GRAY_9900, color.DIM_BLUE),
                                    # size=(None,2)
                                ) ,   
                        ],                     

            ],expand_x=True,expand_y=False,border_width=5,pad=(5,5),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)        
        ], 
        #models_treasury
        [
            sg.Column([       
                    [ 
                        sg.Frame('',[       
                            [
                                sg.Frame('',[    
                                        [
                                            sg.Text(folder,font=FONT_M,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY,size=(20,1)),        
                                            sg.Text(f'{path}/{folders[folder]}',key=f"-target_models_treasury_symlink_{folders[folder]}_path_lbl-",font=FONT_S,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                                        ],                                             
                                        [
                                            sg.In(key=f"-target_models_treasury_symlink_{folders[folder]}_path_in-",
                                                enable_events=True,expand_x=True,expand_y=True,
                                                font=FONT,
                                                text_color=color.LIGHT_GRAY,  
                                                background_color=color.GRAY),

                                                sg.FolderBrowse(button_text=lang_data[LOCAL_BROWSE],k=f"-target_models_treasury_symlink_{folders[folder]}_path_FolderBrowse-",
                                                        button_color=(color.DIM_BLUE, color.GRAY),
                                                        size=(None,2)    
                                                ),   
                                                sg.Button(button_text=lang_data[LOCAL_ADD],
                                                            button_color=(color.DIM_BLUE, color.GRAY),
                                                            key=f"-add_target_models_treasury_symlink_{folders[folder]}_btn-", 
                                                            mouseover_colors=(color.GRAY_9900, color.DIM_BLUE),
                                                            disabled=False if preference_models_treasury_path else True
                                                            
                                                            ),                                                                                    
                                        ],  
                                    ],expand_x=True,expand_y=False,border_width=0,relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)  
                                ] 
                            ],expand_x=True,expand_y=False,border_width=0,relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)  
                    ]
                    for folder in folders
            ],key='-hub_scroll-',expand_x=True,expand_y=True,pad=(5,5),element_justification="l",background_color=color.DARK_GRAY,scrollable=True,vertical_scroll_only=True)        
        ]        
    ]

    layout = [
            [
                sg.Column(col1, key=PROJECTS_COL_1, element_justification='l', expand_x=True,expand_y=True,visible=True),
                sg.Column(col2, key=PROJECTS_COL_2, element_justification='l', expand_x=True,expand_y=True,visible=True),
            ],          
        ]
    return layout


def events(event,values,window,lang_data):
    if event == CREATE_SYMLINK_BTN:
        source = values[SOURCE_CUSTOM_SYMLINK_PATH_IN]
        target = values[TARGET_CUSTOM_SYMLINK_PATH_IN]
        if source and target:
            res=symlink.create_symlink(source, target, verbose=True, use_rollback=True)
            if res:
                sg.popup_quick_message(lang_data[LOCAL_SYMLINK_CREATED_SUCC],text_color=color.GRAY,background_color=color.DIM_GREEN,font=FONT_H2_BOLD,auto_close_duration=2,keep_on_top=True)
            else:
                sg.popup_quick_message(lang_data[LOCAL_SYMLINK_CREATED_FAIL],text_color=color.GRAY,background_color=color.RED_ORANGE,font=FONT_H2_BOLD,auto_close_duration=2,keep_on_top=True)
        else:
            sg.popup_quick_message(lang_data[LOCAL_SOURCE_TARGET_PATH_EMPTY_MSG],text_color=color.GRAY,background_color=color.RED_ORANGE,font=FONT_H2_BOLD,auto_close_duration=2,keep_on_top=True)

    if event == REMOVE_SYMLINK_BTN:
        target=values[REMOVE_SYMLINK_PATH_IN]
        if target:
            res=symlink.remove_symlink(target,create_folder=True)  
            if res:
                sg.popup_quick_message(lang_data[LOCAL_SYMLINK_REMOVING_SUCC],text_color=color.GRAY,background_color=color.DIM_GREEN,font=FONT_H2_BOLD,auto_close_duration=2,keep_on_top=True)
            else:
                sg.popup_quick_message(lang_data[LOCAL_SYMLINK_REMOVING_FAIL],text_color=color.GRAY,background_color=color.RED_ORANGE,font=FONT_H2_BOLD,auto_close_duration=2,keep_on_top=True)
        else:
            sg.popup_quick_message(lang_data[LOCAL_TARGET_PATH_EMPTY_MSG],text_color=color.GRAY,background_color=color.RED_ORANGE,font=FONT_H2_BOLD,auto_close_duration=2,keep_on_top=True)
        
    if event == SET_MODEL_TREASURY_FOLDER_BTN:
        # print('models_treasury_path',values[MODEL_TREASURY_PATH_IN])
        jt.save_preference('models_treasury_path',values[MODEL_TREASURY_PATH_IN])
        path = jt.load_preference('models_treasury_path')            
        sg.popup_quick_message(lang_data[LOCAL_TREASURY_CREATED_MSG],text_color=color.GRAY,background_color=color.DIM_GREEN,font=FONT_H2_BOLD,auto_close_duration=2,keep_on_top=True)

        os.makedirs(path, exist_ok=True)
        for folder in folders:
            folder_path = os.path.join(path, folders[folder])
            os.makedirs(folder_path, exist_ok=True)            
            lbl_elem_key = f"-target_models_treasury_symlink_{folders[folder]}_path_lbl-"
            window[lbl_elem_key].update(f"{path}/{folders[folder]}")
            window[f"-add_target_models_treasury_symlink_{folders[folder]}_btn-"].update(disabled=False)


    if event.startswith("-add_target_models_treasury_symlink_") and event.endswith("_btn-"):
        path = jt.load_preference('models_treasury_path')            
        pattern = r"-add_target_models_treasury_symlink_(\w+)_btn-"
        match = re.search(pattern, event)
        if match:
            folder_name = match.group(1)
            target_folder = values[f'-target_models_treasury_symlink_{folder_name}_path_in-']
            source_folder =f"{path}/{folder_name}"
            if target_folder:
                res=symlink.create_symlink(source_folder, target_folder, verbose=True, use_rollback=True)
                if res:
                    sg.popup_quick_message(lang_data[LOCAL_SYMLINK_CREATED_SUCC],text_color=color.GRAY,background_color=color.DIM_GREEN,font=FONT_H2_BOLD,auto_close_duration=2,keep_on_top=True)
                else:
                    sg.popup_quick_message(lang_data[LOCAL_SYMLINK_CREATED_FAIL],text_color=color.GRAY,background_color=color.RED_ORANGE,font=FONT_H2_BOLD,auto_close_duration=2,keep_on_top=True)
            else:
                sg.popup_quick_message(lang_data[LOCAL_TARGET_PATH_EMPTY_MSG],text_color=color.GRAY,background_color=color.RED_ORANGE,font=FONT_H2_BOLD,auto_close_duration=2,keep_on_top=True)
