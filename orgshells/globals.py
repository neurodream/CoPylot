import orgshells
import subprocess
from pathlib import Path

root_path = Path(orgshells.__file__).parents[1]

def start():
    subprocess.call(['sh', root_path/"startup.sh"])

def done():
    subprocess.call(['sh', root_path/"issuework_finished.sh"])

def lit():
    subprocess.call(['sh', root_path/"issuework_literature.sh"])