import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *

nav_tab_mouseover_colors=(color.DARK_GRAY,color.DIM_BLUE)
nav_tab_button_color=(color.DIM_BLUE,color.DARK_GRAY)
nav_tab_button_active_color=(color.DARK_GRAY,color.DIM_BLUE)

def create_layout(lang_data,languages):
    native_name = lang_data[LOCAL_NATIVE]
    Projects_local = lang_data[LOCAL_PROJECTS]
    System_stats_local = lang_data[LOCAL_SYSTEM_MONITOR]
    AiPanic_local = lang_data[LOCAL_AIPANIC]
    Settings_local = lang_data[LOCAL_SETTINGS]
    About_local = lang_data[LOCAL_ABOUT]
    layout = [
        [
            sg.Frame('', [
                [
                    sg.Button(Projects_local,k=PROJECTS_TAB_BTN,disabled=False,font=FONT,expand_x=True,size=(15,2),button_color=nav_tab_button_active_color,mouseover_colors=nav_tab_mouseover_colors),
                    sg.Button(System_stats_local,visible=False,disabled=True,k=SYSTEM_STATS_TAB_BTN,font=FONT,expand_x=True,size=(20,2),button_color=nav_tab_button_color,mouseover_colors=nav_tab_mouseover_colors),
                    sg.Button(Settings_local,visible=False,disabled=True,k=SETTINGS_TAB_BTN,font=FONT,expand_x=True,size=(10,2),button_color=nav_tab_button_color,mouseover_colors=nav_tab_mouseover_colors),
                    sg.Button(AiPanic_local,disabled=True,k=AIPANIC_TAB_BTN,font=FONT,expand_x=True,size=(10,2),button_color=nav_tab_button_color,mouseover_colors=nav_tab_mouseover_colors),
                    sg.Button(About_local,k=ABOUT_TAB_BTN,font=FONT,expand_x=True,size=(10,2),button_color=nav_tab_button_color,mouseover_colors=nav_tab_mouseover_colors),                    
                    # sg.Push(),
                    sg.Combo(languages, default_value=native_name, s=(1, 20), enable_events=True, readonly=True, k=SET_LANGUAGE, expand_x=True, expand_y=True,
                              font=FONT,text_color=color.DIM_BLUE,button_background_color=color.DARK_GRAY,button_arrow_color=color.DARK_GRAY),
                ],
            ], expand_x=True,key='-nav-', expand_y=False, border_width=0, relief=sg.RELIEF_FLAT, element_justification="c", background_color=color.GRAY_9900)
        ]
    ]

    return layout

def handle_tab_event(event, tab_elements, tab_btn_elements, active_color, inactive_color):
  
    # if event == "-system_stats_tab-":
    #     stop_event.clear()
    #     t = threading.Thread(target=system_stats_monitor, args=(stop_event,2,))
    #     t.start()
    # else:
    #     stop_event.set()
    for tab_key in tab_elements:
        is_target = tab_key == event
        for element in tab_elements[tab_key]:
            element.update(visible=is_target)
        tab_btn_elements[tab_key].update(button_color=(active_color if is_target else inactive_color))    