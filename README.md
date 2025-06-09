# 🧠 Mutual Watchdog System in Python

This project demonstrates a **Mutual Watchdog** system — two Python programs that monitor each other and ensure continuous execution. If either process is terminated, the other restarts it automatically.

## 🔍 How It Works

There are two scripts:

- `watchdog_program1.py` — watches `watchdog_program2.py`
- `watchdog_program2.py` — watches `watchdog_program1.py`

Each script:
- Checks whether its counterpart is running.
- If not, restarts the other script.
- Limits the number of restart attempts to prevent a fork bomb.
- Uses absolute paths and logging for reliability.

This can be used for lightweight fault tolerance in personal or embedded projects.

---

## 💻 Technologies Used

- Python 3.x
- `subprocess` for process management
- Cross-platform compatible (Windows/Linux/macOS)
- Logging with `logging` module

---

## 📂 File Structure

```text
.
├── watchdog_program1.py
├── watchdog_program2.py
├── watchdog1.log
├── watchdog2.log
├── .gitignore
└── README.md


---

## 🔍 How It Works

Each script:

- Uses `subprocess` to monitor the other program.
- Checks running processes using:
  - `tasklist` on Windows
  - `pgrep` on Linux/macOS
- Logs events to a separate log file.
- Uses an absolute path to avoid issues with relative location.
- Caps restarts to avoid infinite loops (fork bomb protection).

---

## 🧪 Use Cases

- Fault-tolerant service monitoring
- Mutual dependency services
- Embedded systems watchdog
- Educational OS/process control example

---

## 💻 Setup and Usage

> ⚠️ **WARNING:** This is for *controlled environments* only.

### 1. Install Python

Ensure Python 3 is installed:
```bash
python3 --version

