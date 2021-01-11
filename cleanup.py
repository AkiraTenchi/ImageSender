import os
from pathlib import Path

def cleanupDir(path):
    entries = Path(path)
    for entry in entries.iterdir():
        if entry.is_dir():
            cleanupDir(path + entry.name + "/")
        elif entry.name.endswith(".mp4") or entry.name.endswith(".webm") or entry.name.endswith(".gif") or entry.stat().st_size > 7900000:
            if os.path.isfile(path + entry.name):
                os.remove(path + entry.name)


cleanupDir("./")
