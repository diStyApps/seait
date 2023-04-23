import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *    
import time
import webbrowser
from threading import Thread
from util.creations_data import creations_data
import requests

# url = "http://seait.surge.sh/creations_data.json"

# response = requests.get(url)

# if response.status_code == 200:
#     creations_data = response.json()
# else:
#     print(f"Failed to fetch JSON data: {response.status_code}")
#     creations_data = []

def create_layout(lang_data):
    return sg.Frame('',[     
                            [
                                sg.Text("YOUR CREATION",expand_x=True,font=FONT,text_color=color.PURPLE,background_color=color.GRAY_1111,justification="c"),
                            ],  
                            [
                                sg.Frame('',[     
                                    [
                                        sg.Button("@intoinstgram",k="-creator_url-",
                                                  expand_x=True,expand_y=False,mouseover_colors=(color.DARK_GRAY,color.PURPLE),button_color=(color.DARK_GRAY,color.PURPLE),pad=(2,2)),
                                    ], 
                                    [
                                        sg.Button("Send to seait.create@gmail.com",size=(25,None),
                                                            expand_x=True,expand_y=False,mouseover_colors=(color.PURPLE,color.DARK_GRAY),button_color=(color.PURPLE,color.DARK_GRAY),pad=(2,2),
                                                            disabled=True,disabled_button_color=(color.PURPLE,color.DARK_GRAY)),                                                   
                                    ],                                     
                                    [
                                        sg.Image(creations_data[0]['creation'],visible=True,key='-image_carousel-',background_color=color.DARK_GRAY,expand_x=True,expand_y=False,pad=(2,2)),
                                    ],  
                                ],expand_x=False,expand_y=False,border_width=0,size=(550,350),relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.PURPLE)
                            ],                                  
                ],expand_x=True,expand_y=False,border_width=0,relief=sg.RELIEF_FLAT,element_justification="c",background_color=color.GRAY_1111)   

def update_image(window, interval=5):
    try:
        creation_index = 0
        while not window["-image_carousel-"].metadata:
            creation = creations_data[creation_index]
            window['-image_carousel-'].update(creation["creation"])
            window['-creator_url-'].update(creation["url"])
            creation_index = (creation_index + 1) % len(creations_data)
            time.sleep(interval)
    except:
        pass

def start(window,interval):
    Thread(target=update_image, args=(window,interval,), daemon=True).start() 

def stop_carousel(window):
    window["-image_carousel-"].metadata = True

def buttons(window,event):
        if event == "-creator_url-":
            webbrowser.open(window[event].GetText())      



