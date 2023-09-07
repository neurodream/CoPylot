"""
(ChatGPT:) In this script:

We use subprocess.getoutput to get the branch name.
We replaced shell echo commands with Python's print function.
The shell read command is replaced by Python's input function to get user input.
The sourced shell scripts are executed using subprocess.run with shell=True and executable="/bin/bash" parameters.
At the end of the script, input() is used to wait for a user action before the script exits, similar to the read command in the original script.
TODO Remember to handle potential errors and exceptions in the real application, possibly by capturing the output of the subprocess.run calls and checking if the commands were successful.
"""

import subprocess
import os

# Load .bashrc (same caution as before applies)
subprocess.run(["source", "~/.bashrc"], shell=True, executable="/bin/bash")

# Get the current branch name
branch_name = subprocess.getoutput("git rev-parse --abbrev-ref HEAD")

# Logic to decide whether to start with a new issue or continue with the existing one
if branch_name == "main":
    subprocess.run(["source", "scripts/shell/issuework_begin.sh"], shell=True, executable="/bin/bash")
else:
    print("You are currently on an issue branch,")
    print("meaning you have local unpushed changes.")
    print("It is RECOMMENDED to finish this issue before starting a new one")
    print("    to avoid pull request chaos.")
    continue_yn = input("Do you want to continue working on this issue? [Y/n]")
    
    if continue_yn.lower() == "n":
        print("WARNING: pull request chaos imminent.")
        print("IMPORTANT TO FINISH ISSUES YOU ARE IN MIDDLE OF FIXING ASAP.")
        subprocess.run(["source", "scripts/shell/issuework_begin.sh"], shell=True, executable="/bin/bash")
    else:
        print(f"you are now continuing to work on {branch_name}. happy coding :)")
    
    subprocess.run(["source", "scripts/shell/issuework_setup_env.sh"], shell=True, executable="/bin/bash")

# Wait for user input to prevent script from exiting immediately
input()