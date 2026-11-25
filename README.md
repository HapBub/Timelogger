# Timelogger

Two small Python scripts that write the current date and time to a text file every time you run them.

## Scripts

- **`log.py`** prints the current time and appends it to `log.txt`.
- **`advancedlog.py`** does the same, appends to `advancedlog.txt`, and prints any command-line arguments you pass.

## Usage

    python3 log.py
    python3 advancedlog.py hello world

Each run adds a timestamp like `01/06/2023 14:30:05` to the log file, one entry per line.

By default the log files are saved in the same folder as the scripts. To use another folder, set the `TIMELOGGER_DIR` environment variable:

    TIMELOGGER_DIR=/path/to/folder python3 log.py

The folder is created if it doesn't exist.

## Notes

- Personal learning project from 2023, since cleaned up.
- `advancedlog.py` prints the arguments but does not save them to the log.
