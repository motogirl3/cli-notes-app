
import json

FILE_NAME = "notes.json"

def load_notes():
    try:
        with open(FILE_NAME, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_notes(notes):
    with open(FILE_NAME, "w") as f:
        json.dump(notes, f, indent=2)
