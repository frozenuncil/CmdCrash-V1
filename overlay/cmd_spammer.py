import subprocess
import time



def spam_cmd_windows():
    for _ in range(100):
        subprocess.Popen("start cmd", shell=True)
        
