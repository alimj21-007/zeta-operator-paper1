"""
logger.py
---------
Utility for logging output generation history to log.txt.
"""

from datetime import datetime

def log_entry(filename: str, action: str, description: str, logfile: str = "log.txt"):
    """
    Append a new entry to the log file.

    Parameters
    ----------
    filename : str
        Name of the file being created or updated.
    action : str
        Action performed, e.g., 'created' or 'updated'.
    description : str
        Brief description of the action.
    logfile : str, optional
        Path to the log file (default 'log.txt').

    Notes
    -----
    Each log entry is formatted as:
    [timestamp] filename - action - description
    """
    ts = datetime.now().isoformat(timespec="seconds")
    entry = f"[{ts}] {filename} - {action} - {description}\n"
    with open(logfile, "a", encoding="utf-8") as f:
        f.write(entry)
