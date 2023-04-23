
import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *
import util.support as support
import util.repos as repos
import util.icons as ic

def create_layout(lang_data,languages):
    native_name = lang_data[LOCAL_NATIVE]

    layout = [
            [
                sg.Frame('',[  
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
                                        
                        ],expand_x=False,expand_y=False,size=(500,100),border_width=5,pad=(5,5),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
                    ],    
                    # [
                    #     sg.Frame('',[       
                    #             [
                    #                 sg.Image(data=ic.args,background_color=color.DARK_GRAY),
                    #                 sg.Text("Your creations",font=FONT,text_color=color.LIGHT_GRAY,background_color=color.DARK_GRAY),
                    #             ],  
                    #             [
                    #                 sg.Checkbox("Show 'Your creations' carousel on startup",
                    #                              default=True,text_color=color.DIM_BLUE,background_color=color.GRAY,
                    #                                k='-SHOW_CREATIONS_CAROUSEL-',enable_events=True, expand_x=True, expand_y=False)
                    #             ],  
                                        
                    #     ],expand_x=False,expand_y=False,size=(500,100),border_width=5,pad=(5,5),relief=sg.RELIEF_FLAT,element_justification="l",background_color=color.DARK_GRAY)
                        
                    # ],                                                    
                ],expand_x=True,expand_y=True,border_width=0,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="l")
            ],  
        ]
    return layout

def events(event):
    if event == '-SHOW_CREATIONS_CAROUSEL-':
        print(event)