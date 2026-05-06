def main():
    print("Notes App")

if __name__ == "__main__":
    main()

from app.notes import NotesApp

def main():
    app = NotesApp()
    app.add_note("Test")
    app.show_notes()

while True:
    print("1. Add")
    print("2. Show")
    print("3. Exit")
input()
