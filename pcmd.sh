#!/bin/bash

# Check if the argument is provided
if [ "$#" -lt 1 ]; then
    echo "Usage: $0 <key> [additional args...]"
    exit 1
fi

# Get the first argument (key)
key="$1"
shift  # Remove the first argument from the list

# Example: Run the Python script with the provided argument and additional args
python_script="/home/usr/path/to/commander.py"

# List of arguments that should NOT run in the background
no_background=("cli" "stay" "task5" "pwd" "py" "run")

# Check if the provided argument is in the list
if [[ " ${no_background[@]} " =~ " $key " ]]; then
    # Run the Python script without backgrounding
    python "$python_script" "$key" "$@"
else
    # Run the Python script in a new subprocess and disown it
    nohup python "$python_script" "$key" "$@" >/dev/null 2>&1 & disown
    # Optionally, print a message indicating that the process is running in the background
    echo "Command started in the background."
fi

