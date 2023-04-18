VERSION = '0.0.8'
APP_TITLE = f"Super Easy AI Installer Tool - Ver {VERSION}"


FONT = 'Arial 12'
FONT_H1 = 'Arial 14'
FONT_H2_BOLD = 'Arial 14 bold'
FONT_H1_BOLD = 'Arial 18 bold'



#nav 
PROJECTS_COL_1 = '-projects_col_1-'
PROJECTS_COL_2 = '-projects_col_2-'
ABOUT_COL = '-about_col-'
SYSTEM_INFO_COL = '-system_stats_col-'

#layout
PROJECTS_LIST_MENU = '-projects_list_menu-'
PROJECTS_COL_PLACEHOLDER = '-projects_col_placeholder-'


#nav buttons
PROJECTS_TAB_BTN = '-projects_tab-'
SYSTEM_STATS_TAB_BTN = '-system_stats_tab-'
AIPANIC_TAB_BTN = '-aipanic_tab-'
SETTINGS_TAB_BTN = '-settings_tab-'
ABOUT_TAB_BTN = '-about_tab-'



SELECTED_PROJECT = '-selected_project_'
SELECT_PROJECT = '-select_project_'

SET_APP_ARGS = "-set_app_args-"
RUN_APP_FUNC = "-run_app_func-"
SET_PROJECT_PATH = "-set_project_path-"
ACTIVATE_PROJECT_PATH = "-activate_project_path-"

SELECT_APP = "-select_app_"
SELECTED_APP = "-selected_app_"


USE_PRE_INSTALLED_VERSION_BTN = '-use_pre_installed_version_btn-'

INSTALL_GIT_BUTTON = '-install_git_btn-'
INSTALLED_GIT_VERSION_LBL = '-installed_git_version_lbl-'

INSTALL_PYTHON_BUTTON = '-install_python_btn-'
INSTALLED_PYTHON_VERSION_LBL = '-installed_python_version_lbl-'


DEP_APP_GIT_INSTALLED_VERSION_FRAME_KEY = '-dep_app_git_installed_version_frame-'
PRE_INSTALLED_VERSION_LBL = '-pre_installed_version_lbl-'

INSTALLERS_PYTHON_PATH = 'data\installers\python-3.10.6-amd64.exe'
INSTALLERS_GIT_PATH = 'data\installers\Git-2.40.0-64-bit.exe'
PRE_INSTALLED_PYTHON_PATH = 'data\Python3106\python.exe'


CHECK_UPDATE_BTN_KEY = '-check_update_btn-'
UPDATE_AVAILABLE_LBL_KEY = '-update_available_lbl-'
# CHECK_UPDATE_BTN_KEY = '-check_update_btn-'

LATEST_RELEASE_URL = "https://github.com/diStyApps/seait/releases/latest"
LATEST_RELEASE_CIVITAI_URL = "https://github.com/diStyApps/seait/releases/latest"
CHECK_UPDATE_URL = "https://github.com/diStyApps/seait/releases"
MODEL_URL_1_5 = "https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors"

#power_usage
SYSTEM_STATS_GPU_POWER_USAGE_LBL_KEY = '-system_stats_gpu_power_usage_lbl'
SYSTEM_STATS_GPU_VRAM_LBL_KEY = '-system_stats_gpu_vram_lbl'
SYSTEM_STATS_GPU_TEMP_LBL_KEY = '-system_stats_gpu_temp_lbl'
SYSTEM_STATS_GPU_NAME_LBL_KEY = '-system_stats_gpu_name_lbl'
SYSTEM_STATS_CPU_USAGE_PRECENT_LBL_KEY = '-system_stats_cpu_usage_precent_lbl'
SYSTEM_STATS_RAM_USAGE_LBL_KEY = '-system_stats_ram_usage_lbl'




LOCALIZATION_PATH = "data/localizations/"

LEAVE_A_LIKE_STAR_TXT_KEY = '-leave_a_like_star_txt_key-'
SET_LANGUAGE = '-set_language_key-'

INSTALLS_TAB_RTL_KEY = '-installs_tab_rtl-'
LAUNCHER_TAB_RTL_KEY = '-launcher_tab_rtl-'
C1_INSTALLS_RTL_KEY = '-c1_installs_rtl-'
C2_INSTALLS_RTL_KEY = '-c2_installs_rtl-'
C1_LAUNCH_RTL_KEY = '-c1_launch_rtl-'
C2_LAUNCH_RTL_KEY = '-c2_launch_rtl-'

CN_MODELS = [
    "cldm_v15.yaml",
    "cldm_v21.yaml",
    "image_adapter_v14.yaml",
    "sketch_adapter_v14.yaml",
    "t2iadapter_style_sd14v1.yaml",
    "t2iadapter_color_sd14v1.yaml",
    "t2iadapter_keypose_sd14v1.yaml",
    "diff_control_sd15_canny_fp16.safetensors",
    "diff_control_sd15_depth_fp16.safetensors",
    "diff_control_sd15_hed_fp16.safetensors",
    "diff_control_sd15_mlsd_fp16.safetensors",
    "diff_control_sd15_normal_fp16.safetensors",
    "diff_control_sd15_openpose_fp16.safetensors",
    "diff_control_sd15_scribble_fp16.safetensors",
    "diff_control_sd15_seg_fp16.safetensors",
    "t2iadapter_canny_sd14v1.pth",
    "t2iadapter_color_sd14v1.pth",
    "t2iadapter_depth_sd14v1.pth",
    "t2iadapter_keypose_sd14v1.pth",
    "t2iadapter_openpose_sd14v1.pth",
    "t2iadapter_seg_sd14v1.pth",
    "t2iadapter_sketch_sd14v1.pth",
    "t2iadapter_style_sd14v1.pth",
    "coadapter-canny-sd15v1.pth",
    "coadapter-color-sd15v1.pth",
    "coadapter-depth-sd15v1.pth",
    "coadapter-fuser-sd15v1.pth",
    "coadapter-sketch-sd15v1.pth",
    "coadapter-style-sd15v1.pth"    
]
project_args = {
    # 1: ['--autolaunch', '--theme=dark'],
    1: [],
    # 2: ['--web'],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [],
    7: [],
    8: [],
    9: [],
}

# LOCALIZATION
LOCAL_YES = "Yes"
LOCAL_NO = "No"
LOCAL_LANG = "lang"
LOCAL_NATIVE = "native"
LOCAL_PROJECTS = "Projects"
LOCAL_SYSTEM_MONITOR = "System Monitor"
LOCAL_AIPANIC = "AiPanic"
LOCAL_SETTINGS = "Settings"
LOCAL_ABOUT = "About"
LOCAL_CHECK_FOR_UPDATE = "Check for Update"
LOCAL_NONE = "None"
LOCAL_INSTALLED = "Installed"
LOCAL_INSTALL = "Install"
LOCAL_LAUNCH = "Launch"
LOCAL_UNINSTALL = "Uninstall"
LOCAL_UPDATE = "Update"
LOCAL_DELETE_VENV = "Delete venv"
LOCAL_CREATE_VENV = "Create venv"
LOCAL_INSTALLED_VERSION = "Installed Version"
LOCAL_INSTALLING_AND_LAUNCHING = "Installing and launching"
LOCAL_LAUNCHING = "Launching"
LOCAL_LAUNCHED = "Launched"
LOCAL_PRE_INSTALLED = "Pre installed"
LOCAL_USE_PRE_INSTALLED = "Use pre installed"
LOCAL_ARGUMENTS = "Arguments"
LOCAL_SETUP = "Setup"
LOCAL_CUSTOM = "Custom"
LOCAL_DOWNLOAD_MODELS = "Download Models"
LOCAL_UPDATE_AVAILABLE = "Update available"
LOCAL_NO_UPDATE_AVAILABLE = "No update available - latest version"
LOCAL_COULD_NOT_FIND_VERSION = "Could not find version information"
LOCAL_CPU_USAGE = "CPU Usage"
LOCAL_RAM_USAGE = "RAM Usage"
LOCAL_TEMPERATURE = "Temperature"
LOCAL_VRAM_USAGE = "VRAM Usage"
LOCAL_POWER_USAGE = "Power Usage"
LOCAL_LIKE_STAR = "Don't forget to leave a like/star."
LOCAL_INCOMPLETE = "isIncomplete"

LOCAL_SET_CUSTOM_PROJECT_PATH = "Set custom project path"
LOCAL_IF_NOT_ACTIVATED = "If not activated"
LOCAL_WILL_USED= "will be used"

LOCAL_BROWSE= "Browse"
LOCAL_SET_PATH = "Set Path"
LOCAL_ACTIVATE= "Activate"
LOCAL_ACTIVATED= "Activated"




#prefs
PREF_SELECTED_LANG = 'selected_lang'
