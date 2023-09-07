"""
(ChatGPT:) In this Python script:

Shell commands have been replaced with equivalent subprocess.run() calls, and backticks for command substitution have been replaced with subprocess.getoutput() calls to get the output as a Python string.
Shell echo and read commands have been replaced with Python's print and input functions, respectively.
Note the warning about sourcing .bashrc – you may want to reconsider if this is necessary, or handle it in another manner.
I kept the source command at the end for the issuework_setup_env.sh script, but you might want to translate this script to Python too, and replace this call with a function call to the Python equivalent.
TODO Remember, you would likely need to test and possibly adjust the script in a real environment to ensure it functions as expected, and handle any errors that might occur during the subprocess calls.
"""

import subprocess

# Load .bashrc (you might need to reconsider this part as explained previously)
subprocess.run(["source", "~/.bashrc"], shell=True, executable="/bin/bash")

# Get remote URL and environment name from environment.yml
remote_url = subprocess.getoutput("git config --get remote.origin.url")
env_name = subprocess.getoutput("head -n 1 environment.yml | sed 's/name: //'")

# List issues from the repo
subprocess.run(["gh", "issue", "list", "--repo", remote_url])

# Get issue ID from user
issue_ID = input("Enter issue ID (WITHOUT the hashtag #): ")
print("")

# Ensure on branch main to avoid merge conflicts/overwriting (might not be necessary anymore)
subprocess.run(["git", "checkout", "main"])

# Pull most recent state of the main branch
print("\n[COMPUTING] move to most recent state of main branch (in case other people pushed to main in meantime)")
subprocess.run(["git", "pull"])

# Create and checkout to a new branch with issue number
subprocess.run(["git", "checkout", "-b", f"issue_{issue_ID}"])

# Setup the packages from environment
print("\n[COMPUTING] setup the packages from environment")
subprocess.run(["conda", "env", "update", "--name", env_name, "--file", "environment.yml", "--prune"])

# Source another shell script (TODO you might want to replace this with equivalent python code)
subprocess.run(["source", "scripts/shell/issuework_setup_env.sh"], shell=True, executable="/bin/bash")