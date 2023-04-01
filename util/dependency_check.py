import os
import subprocess
import platform

def check_python():
    system_platform = platform.system()
    if system_platform == "Windows":
        username = os.getlogin()
        # Look for Python in the default installation directory
        python_path = f"C:\\Users\\{username}\\AppData\\Local\\Programs\\Python"

        if not os.path.exists(python_path):
            # If Python is not found, look for it in other directories
            paths_to_check = [
                r"C:\Program Files\Python",
                r"C:\Program Files (x86)\Python",
                r"C:\Python",
            ]
            for path in paths_to_check:
                if os.path.exists(path):
                    python_path = path
                    break

        if os.path.exists(python_path):
            versions = [d for d in os.listdir(python_path) if os.path.isdir(os.path.join(python_path, d)) and d.startswith('Python')]
            if versions:
                # print("Python versions installed:")
                for version in versions:
                    version_path = os.path.join(python_path, version, 'python.exe')
                    if os.path.exists(version_path):
                        try:
                            version_output = subprocess.check_output([version_path, "--version"])
                            # print(version_output)
                            # print(f"- {version}: {version_output.decode().strip()}")
                            return version_output.decode().strip().strip()[-6:]

                        except subprocess.CalledProcessError:
                            # print(f"- {version}: Error running 'python --version' command.")
                            pass
                    else:
                        # print(f"- {version}: Error: 'python.exe' not found.")
                        pass
            else:
                # print("Error: No Python versions found in installation directory.")
                pass
        else:
            # print("Error: Python not found.")
            pass
        
    elif system_platform == "Linux":
        user_paths = [
            os.path.expanduser("~/.local/bin"),
            "/usr/local/bin",
            "/usr/bin"
        ]
        python_executables = ["python", "python3"]
        for path in user_paths:
            for executable in python_executables:
                version_path = os.path.join(path, executable)
                if os.path.exists(version_path):
                    try:
                        version_output = subprocess.check_output([version_path, "--version"])
                        print(f"- {executable}: {version_output.decode().strip()}")
                    except subprocess.CalledProcessError:
                        print(f"- {executable}: Error running 'python --version' command.")
        else:
            print("Error: No Python versions found in installation directory.")
    else:
        print("Error: Unsupported system.")

def check_git():
    try:
        git_version = subprocess.check_output(["git", "--version"]).decode().strip()
        # print("Git version:", git_version)
        return git_version
    except subprocess.CalledProcessError:
        # print("Git is not installed.")
        pass
    except FileNotFoundError:
        # print("Git is not installed.")  
        pass  
