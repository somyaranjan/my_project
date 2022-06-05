import os

from click import command
def list_dir():
    if os.name == 'nt':
        command = "dir"
    else:
        command = "ls -l"
    os.system(command)

def update_app():
    if os.name == "nt":
        print('This feature is not available for Windows users.. Sorry..')
    else:
        command = "cd .. && rm -r my_project && git clone http://github.com/somyaranjan/my_project.git"
        os.system(command)
        