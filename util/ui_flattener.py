import os

def flatten_ui_elements(window):
    for widget_key in window.key_dict.keys():
        try: 
            window[widget_key].Widget.config(relief='flat')
        except:
            # print("error",widget_key)
            pass
def repack(widget, option):
    pack_info = widget.pack_info()
    pack_info.update(option)
    widget.pack(**pack_info)

def configure_canvas(event, canvas, frame_id):
    canvas.itemconfig(frame_id, width=canvas.winfo_width())

def configure_frame(event, canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))

def expand_column_helper(column):
    frame_id, frame, canvas = column.frame_id, column.TKFrame, column.canvas
    canvas.bind("<Configure>", lambda event, canvas=canvas, frame_id=frame_id:configure_canvas(event, canvas, frame_id))

def isfile_exist_check(file_path):
    if os.path.isfile(file_path):
        print('isfile_exist_check:',file_path, ' FILE EXIST')
        return True
    if not os.path.isfile(file_path):
        print('isfile_exist_check:',file_path,' FILE NOT EXIST')    
        return False   
    
def isfolder_exist_check(file_path):
    if os.path.exists(file_path):
        # print('isfolder_exist_check:',file_path, ' FOLDER EXIST')
        return True
    if not os.path.exists(file_path):
        # print('isfolder_exist_check:',file_path,' FOLDER NOT EXIST')    
        return False   


