import subprocess
import platform
from json import load
import os
from sys import argv


def load_dirs():
    json_file_path = os.path.join(script_directory, "open_directories.json")
    try:
        with open(json_file_path, "r") as file:
            return load(file)
    except FileNotFoundError:
        print("Error: open_directories.json not found.")
        return {}

def open_file_manager(path):
    system_platform = platform.system()

    if system_platform == 'Linux':
        try:
            subprocess.Popen(['xdg-open', f'{path}'])
        except FileNotFoundError:
            print("Error: xdg-open not found. Opening a file manager window might not work.")
    elif system_platform == 'Darwin':  # macOS
        subprocess.Popen(['open', f'{path}'])
    elif system_platform == 'Windows':
        subprocess.Popen(['explorer', fr'{path}'])
    else:
        print(f"Unsupported platform: {system_platform}. Opening a file manager window might not work.")

if __name__ == "__main__":
    if len(argv) != 2:
        if len(argv) == 1:
            print("please provide a path")
        else:
            print("you can open only one directory at a time")
    else:
        script_directory = os.path.dirname(os.path.abspath(__file__))
        dirs = load_dirs()
        path = dirs[argv[1]]
        open_file_manager(path)
