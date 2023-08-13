import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *    
import util.util as util
    
def dialog_window(title,method,lang_data):
        # method = lang_data[util.remove_special_characters_from_text(get_first_word(method),case='capitalize')]
        method_lang = lang_data[util.remove_special_characters_from_text(method,case='capitalize')]
        event, values = sg.Window('', 
        [
            [
                sg.Frame('',[
                    [
                        sg.Button(f'{method_lang} ?',expand_x=True,expand_y=True,font=FONT_H1_BOLD,disabled_button_color=(color.LIGHT_BLUE, color.DARK_GRAY),disabled=True,border_width=0),
                    ],                        
                    [
                        sg.Button(lang_data[LOCAL_YES],k='-yes_key-',expand_x=True,expand_y=True,s=(5,2),font=FONT_H2_BOLD,button_color=(color.DIM_GREEN,color.DARK_GRAY),border_width=0),
                        sg.Button(lang_data[LOCAL_NO],k='-no_key-',expand_x=True,expand_y=True,s=(5,2),font=FONT_H2_BOLD,button_color=(color.RED_ORANGE, color.DARK_GRAY),border_width=0)
                    ],
                ],expand_x=True,expand_y=True,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.LIGHT_GRAY)                       
            ]
#             if method == 'Install webui extension' else 
#             [
#                 sg.Frame('',[
#                     [
#                         sg.Button(f'Install {title} ?',expand_x=True,expand_y=True,font=FONT_H1_BOLD,disabled_button_color=(color.DIM_GREEN, color.GRAY),disabled=True,border_width=0,
#                                   button_color=(color.DARK_GRAY, color.DARK_GRAY)),
#                     ],                   
#                         [
#                         # Do you wish to install ControlNet WebUI extension? it will also download about 19GB of controlnet adpters models
#                             sg.ML(f"""
# Please select the desired installation option:

# Option 1 (Default): Install ControlNet and download adapter models (approximately 19GB).

# Option 2: Install ControlNet only. (Choose if you already have the adapter models)

# """,
#                             font=FONT_H1,text_color=color.DIM_BLUE,background_color=color.DARK_GRAY,size=(80,8),expand_x=True,expand_y=True,visible=True,no_scrollbar=True,disabled=True,justification='l'),
#                         ],                                                             
#                     [
#                         sg.Button("Option 1",k='-yes_key-',expand_x=True,expand_y=True,s=(25,2),font=FONT_H2_BOLD,button_color=(color.DIM_GREEN,color.DARK_GRAY),border_width=0),
#                         sg.Button("Option 2",k='-yes_key-',expand_x=True,expand_y=True,s=(25,2),font=FONT_H2_BOLD,button_color=(color.DIM_GREEN,color.DARK_GRAY),border_width=0),

#                         sg.Button(lang_data[LOCAL_NO],k='-no_key-',expand_x=True,expand_y=True,s=(5,2),font=FONT_H2_BOLD,button_color=(color.RED_ORANGE, color.DARK_GRAY),border_width=0)
#                     ],
#                 ],expand_x=True,expand_y=True,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.LIGHT_GRAY)       
                 
#             ]        
            if method != 'uninstall' else [
                sg.Frame('',[
                    [
                        sg.Button(f'{method_lang} ?',expand_x=True,expand_y=True,font=FONT_H1_BOLD,disabled_button_color=(color.RED_ORANGE, color.GRAY),disabled=True,border_width=0,
                                  button_color=(color.DARK_GRAY, color.DARK_GRAY)),
                    ],                   
                        [
                            sg.ML(f"""
{lang_data[LOCAL_WARN_PERM_DEL]} 
{title} {lang_data[LOCAL_WARN_CANNOT_BE_RECOVERED]} {lang_data[LOCAL_SURE_WANT_TO_CONTINUE]}
""",
                            font=FONT_H1,text_color=color.RED_ORANGE,background_color=color.DARK_GRAY,size=(80,5),expand_x=True,expand_y=True,visible=True,no_scrollbar=True,disabled=True,justification='c'),
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
