import os
import time
import subprocess
import logging

PROGRAM_NAME = "watchdog_program2.py"
RESTART_COOLDOWN = 10  # seconds
MAX_RESTART_ATTEMPTS = 5

# Setup logging
logging.basicConfig(filename="watchdog1.log", level=logging.INFO,
                    format="%(asctime)s - %(levelname)s - %(message)s")

def get_program_path(program_name):
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), program_name)

def is_program_running(program_name):
    try:
        if os.name == "nt":  # Windows
            output = subprocess.check_output(f'tasklist /FI "IMAGENAME eq python.exe"', shell=True).decode()
            return program_name in output
        else:  # Linux/macOS
            output = subprocess.check_output(['pgrep', '-fl', program_name], text=True)
            return any(program_name in line for line in output.splitlines())
    except subprocess.CalledProcessError:
        return False

def start_program(program_path):
    return subprocess.Popen(["python", program_path],
                            stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL)

if __name__ == "__main__":
    logging.info("Watchdog Program 1 started.")
    program_path = get_program_path(PROGRAM_NAME)
    restart_attempts = 0

    while True:
        if not is_program_running(PROGRAM_NAME):
            logging.warning(f"{PROGRAM_NAME} is not running.")
            if restart_attempts < MAX_RESTART_ATTEMPTS:
                logging.info(f"Restarting {PROGRAM_NAME}...")
                start_program(program_path)
                restart_attempts += 1
            else:
                logging.error("Too many restart attempts. Pausing for cooldown.")
                time.sleep(30)
                restart_attempts = 0
        else:
            restart_attempts = 0  # reset counter if running
        time.sleep(RESTART_COOLDOWN)
