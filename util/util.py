import re
import os

def remove_special_characters_from_text(text,underline=False,case='raw'):

    if case=='lower':
        text = re.sub(r"[^a-zA-Z0-9]"," ",text.lower())
    if case=='upper':
        text = re.sub(r"[^a-zA-Z0-9]"," ",text.upper())
    if case=='capitalize':
        text = re.sub(r"[^a-zA-Z0-9]"," ",text.capitalize())
    if case=='title':
        text = re.sub(r"[^a-zA-Z0-9]"," ",text.title())        
    if case=='raw':
        text = re.sub(r"[^a-zA-Z0-9]"," ",text)

    underline_char = "_"
    space_char = " "

    if underline:
        text = re.sub(" +", underline_char, text)
    else:
        text = re.sub(" +", " ", text)     

    text_start = text[:1]
    text_end = text[-1:] 

    if text_start == underline_char and text_end == underline_char:
        return text[1:-1]
    if text_start == underline_char:
        return text[1:]
    if text_end == underline_char:
        return text[:-1]

    if text_start == space_char and text_end == space_char:
        return text[1:-1]
    if text_start == space_char:
        return text[1:]
    if text_end == space_char:
        return text[:-1]
    else:
        return text
    
def isfile_exist_check(file_path):
    if os.path.isfile(file_path):
        # print('isfile_exist_check:',file_path, ' FILE EXIST')
        return True
    if not os.path.isfile(file_path):
        # print('isfile_exist_check:',file_path,' FILE NOT EXIST')    
        return False   
    
def is_folder_exist_check(file_path):
    if os.path.exists(file_path):
        # print('isfolder_exist_check:',file_path, ' FOLDER EXIST')
        return True
    if not os.path.exists(file_path):
        # print('isfolder_exist_check:',file_path,' FOLDER NOT EXIST')    
        return False       
    

def contains_spaces(file_path):
    return ' ' in file_path

def convert_list_to_string(input_list):
    output_string = ' '.join(input_list)
    return output_string    

def convert_string_to_list(input_string):
    items = input_string.split()
    return items
