from app.storage import load_notes, save_notes

class NotesApp:
    def __init__(self):
     self.notes = load_notes()

def add_note(self, text):
    self.notes.append(text)
    save_notes(self.notes)

def show_notes(self):
    for i, n in enumerate(self.notes, 1):
        print(f"{i}. {n}")
