from util.CONSTANTS import LOCALIZATION_PATH
import json
import os

def set_language(lang_code):
    with open(f"{LOCALIZATION_PATH}{lang_code}.json", "r", encoding="utf-8") as f:
        lang_data = json.load(f)
    return lang_data

def get_language_by_codes():
    language_codes = []
    for filename in os.listdir(LOCALIZATION_PATH):
        if filename.endswith(".json"):
            with open(f"{LOCALIZATION_PATH}{filename}", "r", encoding="utf-8") as f:
                lang_data = json.load(f)
                language_codes.append(lang_data["native"])
    return language_codes

def set_language_by_native(native_name):
    language_ids = {}
    for filename in os.listdir(LOCALIZATION_PATH):
        if filename.endswith(".json"):
            with open(f"{LOCALIZATION_PATH}{filename}", "r", encoding="utf-8") as f:
                lang_data = json.load(f)
                language_ids[lang_data["native"]] = lang_data["id"]
    lang_code = language_ids.get(native_name)
    if lang_code:
        with open(f"{LOCALIZATION_PATH}{lang_code}.json", "r", encoding="utf-8") as f:
            lang_data = json.load(f)
        return lang_data
    else:
        print(f"Language '{native_name}' not found")

def get_language_by_native(native_name):
    language_ids = {}
    for filename in os.listdir(LOCALIZATION_PATH):
        if filename.endswith(".json"):
            with open(f"{LOCALIZATION_PATH}{filename}", "r", encoding="utf-8") as f:
                lang_data = json.load(f)
                language_ids[lang_data["native"]] = lang_data["id"]
    lang_code = language_ids.get(native_name)
    return lang_code