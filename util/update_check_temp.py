import requests
import re
from util.CONSTANTS import *

def check_update_available(current_version):
    r = requests.get(CHECK_UPDATE_URL)
    html_content = r.text
    pattern = re.compile(r'<h2[^>]*class="[^"]*sr-only[^"]*"[^>]*>(.*?)</h2>', re.DOTALL)
    match = pattern.search(html_content)

    if match:
        h2_sr_only = match.group(1)
        version_pattern = re.compile(r"\d+\.\d+(\.\d+)?")
        latest_release = version_pattern.search(h2_sr_only).group()

        if latest_release != current_version:
            return f"Update available: {latest_release}"
        else:
            return f"No update available - latest version: {current_version}"
    else:
        return "Could not find version information"
