
import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *
import util.support as support
import util.repos as repos
import util.icons as ic

def create_layout(lang_data):

    star_like_data = lang_data["Don't forget to leave a like/star."]
    layout = [
            [
                sg.Frame('',[  
                    [
                        sg.Frame('',[       
                            [
                                sg.Image(ic.avatar2,background_color=color.DARK_GRAY),
                            ],                             
                            [
                                sg.Text("diSty",font=FONT,background_color=color.DARK_GRAY,text_color=color.LIGHT_GRAY),
                            ],
                            [support.buttons_layout()],
                            [
                                sg.Text(star_like_data,key=LEAVE_A_LIKE_STAR_TXT_KEY,font=FONT,background_color=color.DARK_GRAY,text_color=color.DIM_GREEN),
                            ],                            
                            [repos.buttons_layout()],    
                            [
                                sg.Text("Progress is impossible without change, and those who cannot change their minds cannot change anything.",
                                        font=FONT,background_color=color.DARK_GRAY,text_color=color.GRAY),
                            ],    
                        ],expand_x=True,expand_y=False,border_width=5,pad=(10,10),relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.DARK_GRAY)
                    ],                                  
                ],expand_x=True,expand_y=True,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color="#2A2929")
            ],  
        ]

    return layout



def set_buttons(event):
    support.buttons(event)

    repos.buttons(event)

def set_language(window, lang_data):
    window[LEAVE_A_LIKE_STAR_TXT_KEY].update(lang_data["Don't forget to leave a like/star."])
