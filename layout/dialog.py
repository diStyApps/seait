import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *    
import util.util as util
    
def dialog_window(title,method,lang_data):
        method = lang_data[util.remove_special_characters_from_text(get_first_word(method),case='capitalize')]
        event, values = sg.Window('', 
        [
            [
                sg.Frame('',[
                    [
                        sg.Button(f'{method} ?',expand_x=True,expand_y=True,font=FONT_H1_BOLD,disabled_button_color=(color.LIGHT_BLUE, color.DARK_GRAY),disabled=True,border_width=0),
                    ],                        
                    [
                        sg.Button(lang_data[LOCAL_YES],k='-yes_key-',expand_x=True,expand_y=True,s=(5,2),font=FONT_H2_BOLD,button_color=(color.DIM_GREEN,color.DARK_GRAY),border_width=0),
                        sg.Button(lang_data[LOCAL_NO],k='-no_key-',expand_x=True,expand_y=True,s=(5,2),font=FONT_H2_BOLD,button_color=(color.RED_ORANGE, color.DARK_GRAY),border_width=0)
                    ],
                ],expand_x=True,expand_y=True,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.LIGHT_GRAY)                       
            ]
        ],modal=True, element_justification='c',no_titlebar=True,background_color=color.DARK_GRAY,auto_size_text=True,).read(close=True)
        if event == '-yes_key-':
            return True
        if event == '-no_key-':
            return False
        

def get_first_word(input_string):
    if not input_string or not isinstance(input_string, str):
        return None

    input_string = input_string.replace('_', ' ')
    first_word = input_string.split()[0]
    return first_word
