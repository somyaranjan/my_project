import os

from click import command
def first():
    if os.name == 'nt':
        command = "dir"
    else:
        command = "ls -l"
    os.system(command)