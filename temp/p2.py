import subprocess
import time
import psutil
import os

p1_name = "p1.py"

def is_running(script_name):
    """Check if a script is running by looking for its filename in running processes"""
    script_name = os.path.basename(script_name)  # Ensure only filename is checked
    for process in psutil.process_iter(attrs=['cmdline']):
        try:
            cmdline = process.info['cmdline']
            if cmdline and any(script_name in os.path.basename(arg) for arg in cmdline):
                return True  # The script is running
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False  # The script is not running

while True:
    if not is_running(p1_name):
        print(f"Starting {p1_name} in a new console...")
        subprocess.Popen(["cmd", "/c", "start", "python", p1_name], shell=True)
    
    time.sleep(5)  # Check every 5 seconds
