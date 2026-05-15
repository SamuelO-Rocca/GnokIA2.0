from datetime import datetime
import os

LOG_FILE_PATH = "project/src/logs/"

def _timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def use_register(User=None, Action=None, Details=None):
    User = User if User is not None else "Unknown User"
    Action = Action if Action is not None else "Unknown Action"
    Details = Details if Details is not None else "No additional details provided."
    way_save = os.path.join(LOG_FILE_PATH, "usage_log.txt")
    with open(way_save, "a", encoding="utf-8") as log_file:
        log_entry = f"{_timestamp()} - User: {User} | Action: {Action} | Details: {Details}\n"
        log_file.write(log_entry)

def register_error(error):
    text = str(error)
    way_save = os.path.join(LOG_FILE_PATH, "error_log.txt")
    with open(way_save, "a", encoding="utf-8") as log_file:
        log_entry = f"{_timestamp()} - Error: {text}\n"
        log_file.write(log_entry)