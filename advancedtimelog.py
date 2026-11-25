"""
advancedtimelog.py
Prints any command-line arguments, then appends the current date and time
to advancedlog.txt.

The log folder defaults to the folder this script is in.
To use another folder, set the TIMELOGGER_DIR environment variable:
    TIMELOGGER_DIR=/path/to/folder python3 advancedlog.py hello world
"""
import os
import sys
from datetime import datetime
from pathlib import Path

LOG_DIR = Path(os.environ.get("TIMELOGGER_DIR", Path(__file__).resolve().parent))
LOG_FILE = LOG_DIR / "advancedlog.txt"


def main() -> None:
    # Day/month/year hour:minute:second
    date_str = datetime.now().strftime("[%d/%m/%Y %H:%M:%S]")

    # Display the arguments (sys.argv[0] is the script name, so skip it)
    args = sys.argv[1:]
    if args:
        for arg in args:
            print("argument ~", arg)
    else:
        print("no arguments")

    LOG_DIR.mkdir(parents=True, exist_ok=True)
    with open(LOG_FILE, "a") as f:
        f.write(date_str + "\n")


if __name__ == "__main__":
    main()
