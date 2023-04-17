import subprocess
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