
import json

FILE_NAME = "notes.json"

def load_notes():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
