import webbrowser
import PySimpleGUI as sg
import util.colors as color
SEAIT_BTN_KEY = '-seait_btn-'
SANDS_BTN_KEY = '-sands_btn-'
SDPSG_BTN_KEY = '-sdpsg_btn-'
SEAIT_REPO_URL = "https://github.com/diStyApps/seait"
SANDS_REPO_URL = "https://github.com/diStyApps/Safe-and-Stable-Ckpt2Safetensors-Conversion-Tool-GUI"
SDPSG_REPO_URL = "https://github.com/diStyApps/Stable-Diffusion-Pickle-Scanner-GUI"
FONT = 'Arial 12'
def buttons_layout():
    layout = sg.Frame('',[
            [
                sg.Button(SEAIT_REPO_URL,k=SEAIT_BTN_KEY,font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN),disabled=False),
            ],          
            [
                sg.Button(SANDS_REPO_URL,k=SANDS_BTN_KEY,font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN),disabled=False),
            ],     
            [
                sg.Button(SDPSG_REPO_URL,k=SDPSG_BTN_KEY,font=FONT,expand_x=True,button_color=(color.LIGHT_GRAY,color.GRAY),mouseover_colors=(color.GRAY_9900,color.DARK_GREEN),disabled=False),
            ],                      
        ],expand_x=True,relief=sg.RELIEF_SOLID,border_width=0,background_color=color.DARK_GRAY,element_justification="c")
    return layout

def buttons(event):
    if event == SEAIT_BTN_KEY:
        webbrowser.open(SEAIT_REPO_URL)     
    if event == SANDS_BTN_KEY:
        webbrowser.open(SANDS_REPO_URL)  
    if event == SDPSG_BTN_KEY:
        webbrowser.open(SDPSG_REPO_URL)          