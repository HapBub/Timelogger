"""
timelog.py
Prints the current date and time and appends it to log.txt.

The log folder defaults to the folder this script is in.
To use another folder, set the TIMELOGGER_DIR environment variable:
    TIMELOGGER_DIR=/path/to/folder python3 log.py
"""
import os
from datetime import datetime
from pathlib import Path

LOG_DIR = Path(os.environ.get("TIMELOGGER_DIR", Path(__file__).resolve().parent))
LOG_FILE = LOG_DIR / "log.txt"


def main() -> None:
    # Day/month/year hour:minute:second
    date_str = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    print(date_str)

    # Create the folder if needed, then append to the file
    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(date_str + "\n")


if __name__ == "__main__":
    main()
