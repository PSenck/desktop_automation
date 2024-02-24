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

def execute_command(cmd, additional_args):
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
        print(f"Error: Failed to execute command '{cmd}': {e}")

def main():
    commands = load_commands()

    while True:
        user_input = input("Enter command (or 'exit' to quit): ")
        print("userinput: ", user_input)
        user_input.strip()
        main_input, *additional_args = user_input.split(" ")
        if main_input == "exit":
            break

        if main_input in commands:
            execute_command(commands[main_input], additional_args)
        else:
            print(f"Error: Unknown command '{main_input}'")

if __name__ == "__main__":
    script_directory = get_script_directory()
    main()