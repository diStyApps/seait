import PySimpleGUI as sg
import util.colors as color
from util.CONSTANTS import *    
import util.installation_status as installation_status
import itertools
import util.icons as ic

def create_project_frame(project):
    return sg.Frame('', [
                [
                    sg.Image(project["image_path"], background_color=color.DARK_GRAY, size=(50, 50), expand_x=False,enable_events=True),
                    sg.Button(project["title"], k=f"-selected_app_quick_{project['id']}_launch_btn-", font=FONT_S, expand_x=True, size=(50, 3), button_color=(color.DARK_GRAY, color.PURPLE)),
                ],
                [
                ],
            ], expand_x=False, expand_y=False, border_width=0, relief=sg.RELIEF_FLAT, element_justification="c", background_color=color.DARK_GRAY)

def create_layout(lang_data, projects):
    filtered_projects = [project for project in projects if project['type'] == "app" and installation_status.check_project(project)]
    project_frames = [create_project_frame(project) for project in filtered_projects]
    project_rows = list(itertools.zip_longest(*[iter(project_frames)] * 2, fillvalue=None))

    rows = [
        [
            # sg.Image(data=ic.args, background_color=color.GRAY,pad=(5,5)),
            sg.Text(lang_data[LOCAL_QUICK_LAUNCH], expand_x=True, font=FONT_H1, text_color=color.PURPLE, background_color=color.GRAY_1111, justification="l"),
        ],
    ]

    for row in project_rows:
        row_elements = [frame for frame in row if frame is not None]
        rows.append([
            sg.Frame('', [row_elements], expand_x=True, expand_y=False, border_width=0,pad=(0,0), relief=sg.RELIEF_FLAT, element_justification="l", background_color=color.GRAY_1111)
        ])

    layout_scrollable = len(filtered_projects) > 12
    return sg.Frame('', [
        [
            sg.Column(rows, element_justification='l', expand_x=True, expand_y=True, visible=True, scrollable=layout_scrollable, vertical_scroll_only=True)
        ],
    ], expand_x=True, expand_y=True, border_width=0, relief=sg.RELIEF_FLAT, element_justification="c", background_color=color.GRAY_1111)
