import os
import platform
import subprocess
import sys

def get_python_version():
    is_windows = platform.system() == "Windows"
    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro

    print(f'Python version is {major}.{minor}.{micro}')
    if is_windows:
        supported_minors = [10]
    else:
        supported_minors = [7, 8, 9, 10, 11]

    if not (major == 3 and minor in supported_minors):
        print(f"""
INCOMPATIBLE PYTHON VERSION
This program is tested with 3.10.6 Python, but you have {major}.{minor}.{micro}.
""")

def get_python_installation():
    PYTHON = os.environ.get('PYTHON', 'python')

    try:
        result = subprocess.run([PYTHON, '-c', 'import sys; print(sys.executable)'],
                                capture_output=True, text=True, check=True)
        python_fullname = result.stdout.strip()
        # print('Python is installed and its path is:', python_fullname)
        return python_fullname
    except (FileNotFoundError, subprocess.CalledProcessError):
        # print("Python is not installed or its path is not set in the system environment.")
        return False

def check_python():
    python_fullname = get_python_installation()

    if python_fullname:
        version_output = subprocess.run([python_fullname, '-V'], capture_output=True, text=True)
        version = version_output.stdout.strip().split()[1]

        return {'version': version, 'path': python_fullname}
    else:
        return False
