import copylot
import os
import subprocess
from pathlib import Path

root_path = Path(copylot.__file__).parents[1]

# Load .bashrc (you might need to reconsider this part as explained previously)
subprocess.run(["source", "~/.bashrc"], shell=True, executable="/bin/bash")

# Get remote URL and environment name from environment.yml
remote_url = subprocess.getoutput("git config --get remote.origin.url")
env_name = subprocess.getoutput("head -n 1 environment.yml | sed 's/name: //'")

def startup():
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
    setup_env()

def start():
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
    setup_env()

def done():
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
    # (TODO error checking might be required)
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

def lit():
    # TODO maybe
    subprocess.call(['sh', root_path/"issuework_literature.sh"])

def setup_env():
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