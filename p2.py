import subprocess
import time
import psutil

p1_name = "p1.py"

def is_running(script_name):
    """Check if a script is running"""
    for process in psutil.process_iter(attrs=['pid', 'name', 'cmdline']):
        try:
            if process.info['cmdline'] and any(script_name in arg for arg in process.info['cmdline']):
                return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

while True:
    if not is_running(p1_name):
        print(f"Starting {p1_name} in a new console...")
        subprocess.Popen(["cmd", "/c", "start", "python", p1_name], shell=True)
    
    time.sleep(5)  # Check every 5 seconds
