
import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *
import util.icons as ic

def create_layout(lang_data,languages):
    native_name = lang_data[LOCAL_NATIVE]

    col1 = [
        [
            sg.Frame('',[       
                        [
                            sg.Image(data=ic.args,background_color=color.DARK_GRAY),
                            sg.Text("Set lanaguge",font=FONT,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                        ],  
                        [
                            sg.Combo(languages, default_value=native_name, s=(1, 20), enable_events=True, readonly=True, k=SET_LANGUAGE, expand_x=True, expand_y=False,
                                    font=FONT,text_color=color.DIM_BLUE,button_background_color=color.DARK_GRAY,button_arrow_color=color.DARK_GRAY),                         
                        ],  
                ],expand_x=True,expand_y=False,border_width=5,pad=(5,5),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY),        
        ],
        
    ]
 
    col2 = [
        [
            sg.Frame('',[       


            ],expand_x=True,expand_y=False,border_width=5,pad=(5,5),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)        
        ],
        
    ]

    layout = [
            [
                sg.Column(col1, key=PROJECTS_COL_1, element_justification='l', expand_x=True,expand_y=True,visible=True),
                sg.Column(col2, key=PROJECTS_COL_2, element_justification='l', expand_x=True,expand_y=True,visible=True),
            ],          
        ]
    
    return layout
