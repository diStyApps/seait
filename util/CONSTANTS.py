VERSION = '0.1.4'
APP_TITLE = f"Super Easy AI Installer Tool - Ver {VERSION}"

FONT_S = 'Arial 8'
FONT_M = 'Arial 9'
FONT_M_B = 'Arial 9 bold'



FONT = 'Arial 12'
FONT_H1 = 'Arial 14'
FONT_H2_BOLD = 'Arial 14 bold'
FONT_H1_BOLD = 'Arial 18 bold'



#nav 
PROJECTS_COL_1 = '-projects_col_1-'
PROJECTS_COL_2 = '-projects_col_2-'
ABOUT_COL = '-about_col-'
SYSTEM_INFO_COL = '-system_stats_col-'

SETTINGS_COL = '-settings_col-'
TOOLBOX_COL = '-toolbox_col-'
#layout
PROJECTS_LIST_MENU = '-projects_list_menu-'
PROJECTS_COL_PLACEHOLDER = '-projects_col_placeholder-'


#nav buttons
PROJECTS_TAB_BTN = '-projects_tab-'
SYSTEM_STATS_TAB_BTN = '-system_stats_tab-'
AIPANIC_TAB_BTN = '-aipanic_tab-'
SETTINGS_TAB_BTN = '-settings_tab-'
TOOLBOX_TAB_BTN = '-toolbox_tab-'
ABOUT_TAB_BTN = '-about_tab-'



SELECTED_PROJECT = '-selected_project_'
SELECT_PROJECT = '-select_project_'

SET_APP_ARGS = "-set_app_args-"
RUN_APP_FUNC = "-run_app_func-"
SELECTED_APP_QUICK = '-selected_app_quick-'
SET_PROJECT_PATH = "-set_project_path-"
ACTIVATE_PROJECT_PATH = "-activate_project_path-"
ADD_PROJECT_FOLDER_NAME = "-add_project_folder_name-"
SAVE_DEFAULT_ARGS= "-save_default_args-"
SELECT_APP = "-select_app_"
SELECTED_APP = "-selected_app_"
INIT_DEFAULT_PROJECT_ARGS = "-init_default_project_args-"




REMOVE_SYMLINK_BTN = "-remove_symlink_btn-"
CREATE_SYMLINK_BTN = "-create_symlink_btn-"
SOURCE_CUSTOM_SYMLINK_PATH_IN = "-source_custom_symlink_path_in-"
TARGET_CUSTOM_SYMLINK_PATH_IN = "-target_custom_symlink_path_in-"
#Models Treasury
MODEL_TREASURY_PATH_IN = "-model_treasury_path_in-"
MODEL_TREASURY_PATH_FOLDER_BROWSE = "-model_treasury_path_FolderBrowse-"
SET_MODEL_TREASURY_FOLDER_BTN = "-set_model_treasury_folder_btn-"
REMOVE_SYMLINK_PATH_IN = "-remove_symlink_path_in-"
SOURCE_CUSTOM_SYMLINK_PATH_FOLDER_BROWSE = "-source_custom_symlink_path_FolderBrowse-"
TARGET_CUSTOM_SYMLINK_PATH_FOLDER_BROWSE = "-target_custom_symlink_path_FolderBrowse-"


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

# LOCALIZATION
LOCAL_YES = "Yes"
LOCAL_NO = "No"
LOCAL_LANG = "lang"
LOCAL_LANG_ID = "id"
LOCAL_NATIVE = "native"
LOCAL_PROJECTS = "Projects"
LOCAL_SYSTEM_MONITOR = "System Monitor"
LOCAL_AIPANIC = "AiPanic"
LOCAL_SETTINGS = "Settings"
LOCAL_TOOLS = "tools"
LOCAL_TOOLBOX = "toolbox"
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
LOCAL_SET_CUSTOM_PROJECT_PATH = "set_custom_project_path"
LOCAL_IF_NOT_ACTIVATED = "If_not_activated"
LOCAL_WILL_USED= "will_be_used"
LOCAL_BROWSE= "browse"
LOCAL_SET_PATH = "set_path"
LOCAL_SET_FOLDER_PROJECT_NAME = "set_folder_project_name"
LOCAL_ACTIVATE= "activate"
LOCAL_ACTIVATED= "activated"
LOCAL_ACTIVATED= "activated"
LOCAL_SAVE = "save"
LOCAL_TEMPORARY_NOT_WORKING_PROPERLY = "Temporary not working properly"
LOCAL_QUICK_LAUNCH = "quick_Launch"
LOCAL_PATH_SPACES_WARNING = "path_spaces_warning"
LOCAL_CHECK_PYTHON_PATH = "check_python_path"
LOCAL_CHECK_PYTHON_PATH_LBL= "-check_python_path_lbl-"
LOCAL_ADD_PROJECT_NAME_FOLDER_TO_PATH = "add_project_name_folder_to_path"
LOCAL_DOWNLOAD_THE_IV = "please_download_the_iv"
PREF_SELECTED_LANG = 'selected_lang'
LOCAL_SOURCE= "Source"
LOCAL_TARGET= "Target"
LOCAL_DESTINATION= "Destination"
LOCAL_ADD= "add"
LOCAL_REMOVE= "remove"
LOCAL_WARNING= "warning"
LOCAL_WARNING_SYMLINK_MSG= "warning_symlink_msg"
LOCAL_SET = "set"
LOCAL_REMOVE_SYMLINK_TOOLTIP = "remove_symlink_tooltip"
LOCAL_MODELS_TREASURY = "models_treasury"
LOCAL_CREATE = "create"
LOCAL_SYMLINK_CREATED_SUCC = "symlink_created_succ"
LOCAL_SYMLINK_CREATED_FAIL = "symlink_created_fail"
LOCAL_SYMLINK_REMOVING_FAIL = "symlink_removing_fail"
LOCAL_SYMLINK_REMOVING_SUCC = "symlink_removing_succ"
LOCAL_SOURCE_TARGET_PATH_EMPTY_MSG = "source_target_path_empty_msg"
LOCAL_TARGET_PATH_EMPTY_MSG = "target_path_empty_msg"
LOCAL_TREASURY_CREATED_MSG = "treasury_created_msg"
LOCAL_CLOSE_RUNNING_PROJECTS = "close_running_projects"