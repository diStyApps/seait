
import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *    

def dialog_window(title,method):
        event, values = sg.Window('', 
        [
            [
                sg.Frame('',[
                    [
                        sg.Button(f'{method} {title} ?',expand_x=True,expand_y=True,font=("Arial", 18, "bold"),disabled_button_color=(color.LIGHT_BLUE, color.DARK_GRAY),disabled=True,border_width=0),
                    ],                        
                    [
                        sg.Button('Yes',expand_x=True,expand_y=True,s=(5,2),font=("Arial", 14, "bold"),button_color=(color.DIM_GREEN,color.DARK_GRAY),border_width=0),
                        sg.Button('No',expand_x=True,expand_y=True,s=(5,2),font=("Arial", 14, "bold"),button_color=(color.RED_ORANGE, color.DARK_GRAY),border_width=0)
                    ],

                ],expand_x=True,expand_y=True,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.LIGHT_GRAY)                       
            ]
        ],
            modal=True, element_justification='c',no_titlebar=True,background_color=color.DARK_GRAY,auto_size_text=True,).read(close=True)
        if event == 'Yes':
            return True
        if event == 'No':
            return False