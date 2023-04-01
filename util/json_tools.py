import json
PREFERENCES_FILE_NAME = 'preferences.json'

class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)


def save_json_file(filename_path,dictionary,add_default_ext=False):
    if add_default_ext:
        with open(f'{filename_path}.json', 'w') as fp:
            json.dump(dictionary, fp,  indent=4,cls=SetEncoder)
    else:
        with open(filename_path, 'w') as fp:
            json.dump(dictionary, fp,  indent=4,cls=SetEncoder)
            
    return read_json_file(filename_path)

def read_json_file(filename_path,add_default_ext=False):
    if add_default_ext:
        with open(f'{filename_path}.json', 'r') as f:
            x = json.load(f) # x is a python dictionary in this case
        return x
    else:
        with open(filename_path, 'r') as f:
            x = json.load(f) # x is a python dictionary in this case
        return x

def read_json_file_full_path(filename_path):
    with open(filename_path, 'r') as f:
        x = json.load(f) # x is a python dictionary in this case
    return x


def save_preference(preference_name,preference_value):
    try:
        file = read_json_file(PREFERENCES_FILE_NAME)
        file[preference_name]=preference_value
        return save_json_file(PREFERENCES_FILE_NAME,file)    
    except FileNotFoundError:
        print(save_preference,'ERROR Create preferences file')
        return False

def get_preference():
    try:
        return read_json_file(PREFERENCES_FILE_NAME)
    except FileNotFoundError:
        print(get_preference,'ERROR Create preferences file')
        return False

def create_preferences_init():
    preferences={
        "init": 0,
        # "usePreInstalledPython": True,
    }
    def create_preferences(preferences):
        save_json_file(PREFERENCES_FILE_NAME,preferences)
    try:
        preferences_file = read_json_file(PREFERENCES_FILE_NAME)
        if preferences_file['init']:
            create_preferences(preferences)
            save_preference('init',0)
        else: 
            # print(create_preferences,'preferences file initialized')
            pass
    except FileNotFoundError:
        print(create_preferences,'creating preferences file ')
        create_preferences(preferences)
        save_preference('init',0)
        # print(create_preferences,'preferences file initialized')


# create_preferences()
# print(save_preference('clip_cuts_threshold',1))

# print(get_preference()['clip_cuts_threshold'])

# print(read_json_file('datatest'))

# cut_number = 'dance2_8d122db6-796d-410f-bf65-5bd2a4370f33_cut_preview_111-'
# print('string',cut_number)

# cut_number2 = cut_number.split('_cut_preview_')

# print('splited',cut_number2)

# id = cut_number2[1]
# print('id',id)


# print(id[:-1])

# # print(cut_number[:1])

# from tqdm import tqdm

# from time import sleep
# # for current_frame in tqdm(range(frame_count)):
    
# #     pass
# with tqdm(total=100) as pbar:
#     for i in range(10):
#         sleep(0.1)
#         pbar.update(10)
# import sys
# print(sys.path[0])

# import sys
# for p in sys.path:
#     print(p)


# import os

# Get the current working directory
# cwd = os.getcwd()
# print(cwd)

# # Print the current working directory
# print("Current working directory: {0}".format(cwd))

# Print the type of the returned object
# print("os.getcwd() returns an object of type: {0}".format(type(cwd)))
# cwd = os.getcwd()
# print(cwd)
# cwd_re =cwd.replace("\\",'/')
# print(cwd_re)
# cwd = os.getcwd()
# cwd_re =cwd.replace("\\",'/')
# id = 'im_42ac76de-7ad0-4ecf-b9ab-c21cf166635e'
# text_fie_path = f'output/{id}/final_clips/cutslist.txt'


# dir = os.listdir(f'{cwd_re}/output/{id}/final_cut/videos/final_clips/')
# if dir:
#     print('files')   
#     for file in os.listdir(f'{cwd_re}/output/{id}/final_cut/videos/final_clips/'):
#         # if file.endswith(".mp4"):
#         string = os.path.join(f"{cwd_re}/output/{id}/final_cut/videos/final_clips/", file)      
#         if string:
#             string = string.split('final_clip_')
#             string = string[1].split('.mp4')
#             int = int(string[0])
#             int = int + 1
#             join_file = f'ffmpeg -y -f concat -safe 0 -i {text_fie_path} -c copy output/{id}/final_cut/videos/final_clips/final_clip_{int}.mp4'
#             print(join_file)         
# else:
#     print('no files')
#     join_file = f'ffmpeg -y -f concat -safe 0 -i {text_fie_path} -c copy output/{id}/final_cut/videos/final_clips/final_clip_1.mp4'
#     print(join_file)



# for file in os.listdir(f'{cwd_re}/output/{id}/final_cut/videos/final_clips/'):
#     # if file.endswith(".mp4"):
#     string = os.path.join(f"{cwd_re}/output/{id}/final_cut/videos/final_clips/", file)

#     # print(type(string))
#     if os.listdir(f'{cwd_re}/output/{id}/final_cut/videos/final_clips/'):
#         print('no files')
#     else:
#         print('else no files')        
    # if string:
    #     string = string.split('final_clip_')
    #     string = string[1].split('.mp4')
    #     int = int(string[0])
    #     int = int + 1
    #     join_file = f'ffmpeg -y -f concat -safe 0 -i {text_fie_path} -c copy output/{id}/final_cut/videos/final_clips/final_clip_{int}.mp4'
    #     print(join_file)
    # else:
    #     join_file = f'ffmpeg -y -f concat -safe 0 -i {text_fie_path} -c copy output/{id}/final_cut/videos/final_clips/final_clip_1.mp4'
    #     print(join_file)

# string='C:/Users/Luna/miniconda/vcis/output/im_42ac76de-7ad0-4ecf-b9ab-c21cf166635e/final_cut/videos/final_clips/final_clip_0.mp4'
# string = string.split('final_clip_')
# string = string[1].split('.mp4')
# int = int(string[0])
# int = int + 1
# print(int)




# string='C:/Users/Luna/miniconda/vcis/output/im_bdc5bee5-ab56-4c6d-b334-3da0814b8f04/videos/selected_clips/selected_clip_1.mp4'
# string = string.split('selected_clip_')
# string = string[1].split('.mp4')
# int = int(string[0])
# int = int + 1
# print(int)


# if event.startswith('-input_files_play_'):
    # get_file_name = event.replace("-input_files_play_",'')

# play -cuts_files_final_play_final_clip_1_im_2c5af93c-a1b8-4a6b-8a7f-9ca28785b9ff-

# if event.startswith('-cuts_files_final_play_final_clip_'):

# event = '-cuts_files_final_play_final_clip_256_im_2c5af93c-a1b8-4a6b-8a7f-9ca28785b9ff-'
# file_id = event.replace("-cuts_files_final_play_final_clip_",'')
# event_value = f'-cuts_files_final_play_input_final_clip_{file_id}'
# print(event_value)
# 122 SS22
# 123 SS23
# 124 SS24
# 125 SS25
# 126 SS26
# 127 SS27
# 128 SS28
# 129 SS29
# 222 FW22
# 223 FW23
# 224 FW24
# 225 FW25
# 226 FW26
# 227 FW27
# 228 FW28
# 229 FW29


# seasons: ['SS22',
#     'FW22',
#     'SS23',
#     'FW23',
#     'SS24',
#     'FW24',
#     'SS25',
#     'FW25',
#     'SS26',
#     'FW26',
#     'SS27',
#     'FW27',
#     'SS28',
#     'FW28',
#     'SS29',
#     'FW29']

# seasons: ['SS22'],

# def return_season_number(season_string):
#     season_string_prefix = season_string[:2]
#     season_string_year = season_string[2:]
    
#     if  season_string_prefix == 'FW':
#         season_string_year = f'2{season_string_year}'
#         season_string_year = int(season_string_year)
#         return season_string_year

#     if  season_string_prefix == 'SS':
#         season_string_year = f'1{season_string_year}'
#         season_string_year = int(season_string_year)
#         return season_string_year

# def return_season_string(season_string):
#     season_string_prefix = season_string[:1]
#     season_string_year = season_string[1:]
    
#     if  season_string_prefix == '2':
#         season_string_year = f'FW{season_string_year}'
#         return season_string_year

#     if  season_string_prefix == '1':
#         season_string_year = f'SS{season_string_year}'
#         return season_string_year


# # print(return_season_number('FW29'))
# # print(return_season_number('SS27'))

# print(return_season_string('223'))
# # print(return_season_string('223'))


# listdir = [
# 'selected_clip_1.mp4', 
# 'selected_clip_10.mp4',
# 'selected_clip_2.mp4', 
# 'selected_clip_3.mp4', 
# 'selected_clip_4.mp4', 
# 'selected_clip_5.mp4', 
# 'selected_clip_6.mp4', 
# 'selected_clip_7.mp4',
# 'selected_clip_8.mp4', 
# 'selected_clip_9.mp4']

# listdir_new = []

# for file in listdir:
#     string = file.split('selected_clip_')
#     string = string[1].split('.mp4')
#     string = string[0]
#     int_count = int(string)    
#     listdir_new.append(int_count)

# print(listdir_new)
# max_height = max(listdir_new)
# print(max_height)

# string = 'C:/Users/Luna/miniconda/vcis/output/lga_d40ce93d-27b1-4d5c-9953-8ef913811339/videos/selected_clips/selected_clip_09.mp4'
# string = string.split('selected_clip_')
# string = string[1].split('.mp4')
# string = string[0]
# int_count = int(string)
# int_count = int_count + 1
# # if int_count > int_count
# print(int_count)

# selected_clip_filename = f'selected_clip_{int_count}.mp4'
# print(selected_clip_filename)

# heights = [
# 1 ,
# 10,
# 2,
# 3,
# 4,
# 5,
# 6,
# 7,
# 8,
# 9,
# ]
# max_height = max(heights)
# print(max_height)

# class student:
# 	name=''
# 	age=0
# 	def __init__(self, name, age):
# 		self.name = name
# 		self.age = age

# s1 = student('Bill', 25)
# s2 = student('Steve', 29)
# s3 = student('Ravi', 26)

# student_list = [s1, s2, s3]
# # student_list.sort() # raise an error

# student_list.sort(key=lambda s: s.name) # sorts using lambda function

# print('Students in Ascending Order:', end=' ')

# for std in student_list:
# 	print(std.name, end=', ')

# # student_list.sort(key=lambda s: s.name, reverse=True) # sorts using lambda function

# # print('Students in Descending Order:', end=' ')

# # for std in student_list:
# # 	print(std.name, end=', ')

# str = 'TODAY.S.RELEASE.r.nNympho.Harley.King.Harley.s.Dick.Cravings.2.8.2022.Cute.Blonde.Huge.Blonde.HugeTits.HugeTits.HugeTits.HugeTits.gif'

# # str = 'TODAY.S.RELEASE.r.nNympho.Harley.King.Harley.s.Dick.Cravings.2.8.2022.Cute.Blonde.HugeTits.BigAss.BigButt.HugeAss.Curvy.CurvyGirl.PAWG.Blonde.POV.gif'


# print(len(str))