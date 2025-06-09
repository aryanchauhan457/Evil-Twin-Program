#Evil Twin Program

import os
import time
import subprocess

program2_name = "program2.py"

def is_program_running(program_name):
    """Check if a program is running using `pgrep` on Unix or `tasklist` on Windows."""
    try:
        if os.name == "nt":  # Windows
            output = subprocess.check_output(f'tasklist | findstr /I {program_name}', shell=True).decode()
        else:  # Linux/Mac
            output = subprocess.check_output(f'pgrep -fl {program_name}', shell=True).decode()

        return program_name in output
    except subprocess.CalledProcessError:
        return False

def start_program(program_name):
    """Start the other program."""
    return subprocess.Popen(["python", program_name], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    print(f"Program 1 is running... Watching {program2_name}")

    while True:
        if not is_program_running(program2_name):
            print(f"{program2_name} is not running. Restarting it...")
            start_program(program2_name)
        time.sleep(5)  # Check every 5 seconds



