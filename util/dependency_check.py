from util.detect_git import check_git
import util.active_python_version as active_python_version
import util.python_versions as python_versions

def detect_python():
    active_python_info = active_python_version.check_python()
    
    if active_python_info:
        return active_python_info
    
    python_versions_info = python_versions.check_python()
    
    if python_versions_info:
        return python_versions_info
    
    return False
