
import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *
import util.icons as ic
import util.json_tools as jt
import util.symlink_creator as symlink
import os
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
main_folder = 'models_treasury'
getcwd = convert_to_backslashes(os.path.abspath(os.getcwd()))
path = convert_to_backslashes(os.path.join(getcwd,main_folder))
if jt.load_preference('models_treasury_path') != None:
    path = jt.load_preference('models_treasury_path')

def create_layout(lang_data,tools):




    tools =[
        "Symlink",
    ]

    col1 = [
        [
            sg.Frame('',[       
                        [
                            sg.Image(data=ic.args,background_color=color.DARK_GRAY),
                            sg.Text("Tools",font=FONT,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                        ],  
                        [
                            sg.Combo(tools, default_value=tools[0], s=(1, 20), enable_events=True, readonly=True, k=SET_LANGUAGE, expand_x=True, expand_y=False,
                                    font=FONT,text_color=color.DIM_BLUE,button_background_color=color.DARK_GRAY,button_arrow_color=color.DARK_GRAY,disabled=False),                         
                        ],  
                ],expand_x=True,expand_y=False,border_width=5,pad=(5,5),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY),        
        ],
        
    ]

    
    col2 = [
        [
            sg.Frame('',[       
                    [
                        sg.Image(data=ic.args,background_color=color.DARK_GRAY),
                        sg.Text("Set Symlink",font=FONT,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                    ],  
                    [
                        sg.Frame('',[       

                        [
                            sg.Text("Source",font=FONT_M_B,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
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
                            sg.Text("Target",font=FONT_M_B,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
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
                                    button_text='Create Symlink',
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
                                sg.Text("Remove",font=FONT_M_B,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                                sg.Text("type the folder path to remove",font=FONT_S,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                            ],                                  
                            [
                                sg.In(key=REMOVE_SYMLINK_PATH_IN,
                                    enable_events=True,expand_x=True,expand_y=True,
                                    font=FONT,
                                    text_color=color.LIGHT_GRAY,  
                                    background_color=color.GRAY),           
                                sg.Button(
                                                button_text='Remove Symlink',
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
                        sg.Text("Models Treasury",font=FONT,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                      
                    ],  

            ],expand_x=True,expand_y=False,border_width=5,pad=(5,5),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)        
        ],     
        [
            sg.Frame('',[        
                        [
                            sg.Text(f"Set Models Treasury",font=FONT_S,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                        ],                                  
                        [
                            sg.In(default_text=path,key=MODEL_TREASURY_PATH_IN,
                                enable_events=True,expand_x=True,expand_y=True,
                                font=FONT,
                                text_color=color.LIGHT_GRAY,  
                                background_color=color.GRAY,  
                                ),
                            sg.FolderBrowse(button_text=lang_data[LOCAL_BROWSE],k=MODEL_TREASURY_PATH_FOLDER_BROWSE,
                                    button_color=(color.DIM_BLUE, color.GRAY),
                                    size=(None,2)    
                                ),                  
                            sg.Button(
                                    button_text='Set',
                                    button_color=(color.DIM_BLUE, color.GRAY),
                                    key=SET_MODEL_TREASURY_FOLDER_BTN, 
                                    expand_x=False, 
                                    mouseover_colors=(color.GRAY_9900, color.DIM_BLUE),
                                    # size=(None,2)
                                ) ,   
                        ],                     

            ],expand_x=True,expand_y=False,border_width=5,pad=(5,5),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)        
        ], 
        #models_treasury            -remove_symlink_btn-22
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
                                                sg.Button(button_text='Add',
                                                            button_color=(color.DIM_BLUE, color.GRAY),
                                                            key=f"-add_target_models_treasury_symlink_{folders[folder]}_btn-", 
                                                            mouseover_colors=(color.GRAY_9900, color.DIM_BLUE)),          
                                                # sg.Button(button_text='Remove',
                                                #                 button_color=(color.DIM_BLUE, color.GRAY),
                                                #                 key=f"-remove_target_models_treasury_symlink_{folders[folder]}_btn-",  
                                                #                 mouseover_colors=(color.GRAY_9900, color.DIM_BLUE))                                                                           
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


def events(event,values,window):
    if event == CREATE_SYMLINK_BTN:
        src= values[SOURCE_CUSTOM_SYMLINK_PATH_IN]
        dst= values[TARGET_CUSTOM_SYMLINK_PATH_IN]
        if src and dst:
            symlink.create_symlink(src, dst, verbose=True, use_rollback=True)
        else:
            sg.popup_error("Source or Target path is empty")

    if event == REMOVE_SYMLINK_BTN:
        dst= values[REMOVE_SYMLINK_PATH_IN]
        symlink.remove_symlink(dst,create_folder=True)
        
    if event == SET_MODEL_TREASURY_FOLDER_BTN:
        print('models_treasury_path',values[MODEL_TREASURY_PATH_IN])
        jt.save_preference('models_treasury_path',values[MODEL_TREASURY_PATH_IN])

        for folder in folders:
            lbl_elem_key = f"-target_models_treasury_symlink_{folders[folder]}_path_lbl-"
            path = jt.load_preference('models_treasury_path')            
            window[lbl_elem_key].update(f"{path}/{folders[folder]}")