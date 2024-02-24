#!/usr/bin/env python3
import sys
import os
import json
import subprocess


def get_script_directory():
    # Get the absolute path of the script
    return os.path.dirname(os.path.abspath(__file__))

def load_commands():
    json_file_path = os.path.join(script_directory, "cmds.json")
    try:
        with open(json_file_path, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: cmds.json not found.")
        return {}

def execute_command_in_background(cmd):
    try:

        if os.getcwd() != script_directory and cmd.startswith("python"):
            splitter = "python3 " if cmd.startswith("python3")  else "python "
            pyfile = cmd.split(splitter, 1)[1]
            cmd = splitter
            cmd += os.path.join(script_directory, pyfile)
        

        if additional_args:
            cmd += " " + " ".join(additional_args)
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()
        print(f"Command '{cmd}' output:")
        print("STDOUT:", stdout)
        print("STDERR:", stderr)
    except Exception as e:
        print(f"Error: Failed to execute command '{cmd}' in the background: {e}")

if __name__ == "__main__":

    script_directory = get_script_directory()
    
    if len(sys.argv) < 2:
        print("Usage: python script.py <key> [additional args...]")
        sys.exit(1)

    key = sys.argv[1]
    additional_args = sys.argv[2:]
    commands = load_commands()

    if key in commands:
        command_to_execute = commands[key]
        execute_command_in_background(command_to_execute)
    else:
        print(f"Error: Unknown key '{key}'. Check your paulcmds.json file.")
