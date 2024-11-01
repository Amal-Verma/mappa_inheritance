import pyuac
import ctypes
import sys
import os
from subprocess import Popen, PIPE

def read_command():
    with open('command.txt', 'r') as file:
        command = file.read().strip()
    return command

def create_batch_file(command):
    with open('batchfile.bat', 'w') as file:
        file.write(command)

def run_batch_file():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    p = Popen('batchfile.bat', cwd=script_dir, stdout=PIPE, stderr=PIPE)
    stdout, stderr = p.communicate()
    print(p.returncode)
    print(stdout.decode())
    print(stderr.decode())
    input("-----Command executed ----- \n Press any key to exit")

def main():
    command = read_command()
    create_batch_file(command)
    run_batch_file()

if __name__ == "__main__":
    if not pyuac.isUserAdmin():
        print("Re-launching as admin!")
        pyuac.runAsAdmin()
    else:        
        main()