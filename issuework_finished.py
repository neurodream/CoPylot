"""
ChatGPT Notes:

I used subprocess.run and subprocess.getoutput to execute shell commands and get their output in Python.
Reading the environment.yml is done using file I/O in Python, and we only read the first line to get the environment name.
The .bashrc sourcing is done with subprocess.run, setting shell=True and executable="/bin/bash". Please be cautious with sourcing .bashrc as it can have unexpected consequences.
The clear command at the end is made OS-agnostic, with different commands used for Windows (cls) and Unix-like systems (clear).
You may want to add error checking to the subprocess calls to ensure they succeed (or handle failures gracefully). You might use the check=True parameter to subprocess.run to have it raise an exception if the command fails.
Python doesn't have a direct way to activate a conda environment within the script since activating an environment is a shell-specific operation. However, the commands are executed in a subprocess where the environment is activated (but this will not affect the Python script's environment). You might need to adjust this section to suit your needs and environment.
"""

import os
import subprocess

# Load .bashrc (Note: Loading bashrc in a script can have unexpected consequences)
subprocess.run(["source", "~/.bashrc"], shell=True, executable="/bin/bash")

# Get various data from git and environment file
branch_name = subprocess.getoutput("git rev-parse --abbrev-ref HEAD")
issue_id = branch_name.split('_')[1] if '_' in branch_name else ''
remote_url = subprocess.getoutput("git config --get remote.origin.url")
user_name = subprocess.getoutput("git config user.name")

# Get environment name from environment.yml
with open("environment.yml", 'r') as file:
    env_name = file.readline().replace("name: ", "").strip()

# Get issue title to use as commit message
commit_msg = subprocess.getoutput(f"gh issue view {issue_id} --json title --jq '.title'")

# Capture all new packages installed while working on the issue
# (Note: error checking might be required)
subprocess.run(f"conda activate {env_name} && conda env export > environment.yml", shell=True, executable="/bin/bash")

# Commit and push changes
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", commit_msg])
subprocess.run(["git", "push", "origin", branch_name])

# Create a pull request and switch back to main branch
subprocess.run(["gh", "pr", "create", "-b", f"closes #{issue_id}", "-a", user_name, "-t", branch_name, "--repo", remote_url])
subprocess.run(["git", "branch", "-m", f"PULL_REQUESTED_issue_{issue_id}"])
subprocess.run(["git", "checkout", "main"])

# Clear the console (might work differently on Windows)
if os.name == 'nt':
    os.system('cls')
else:
    os.system('clear')