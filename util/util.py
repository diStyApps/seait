import re

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