"""
ChatGPT Explanation:

We are using subprocess.getoutput() to execute the command and get its output as a Python string.
subprocess.run() is used to run the various commands.
The conda activate command is being run with shell=True to allow shell built-in commands. Please note that the conda activate may not work properly with subprocess.run() and you might need to use a Conda Python API or another method to activate the environment in Python.
The pip install -e . command installs the current package (i.e., the package that the script is in) in editable mode.
The code . command opens the current folder in Visual Studio Code.
The clear terminal command at the end is optional and OS-specific as noted in the comments.
TODO You should test and adapt the script to ensure it meets your needs and handles any errors that may occur.
"""

import subprocess

# Get environment name from environment.yml
env_name = subprocess.getoutput("head -n 1 environment.yml | sed 's/name: //'")

# Activate environment
subprocess.run(["conda", "activate", env_name], shell=True)

# Make own package usable
subprocess.run(["pip", "install", "-e", "."])

# Open Visual Studio Code
subprocess.run(["code", "."])

# You mentioned a TODO about clearing, not sure what was intended here.
# If you want to clear the terminal, it would be OS-specific.
# On Windows, you might use 'cls', and on UNIX-like systems, 'clear'.
# subprocess.run("clear", shell=True)  # UNIX-like
# subprocess.run("cls", shell=True)  # Windows