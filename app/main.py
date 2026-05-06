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
from app.notes import NotesApp

def main():
    app = NotesApp()

    while True:
        print("\n1. Add note")
        print("2. Show notes")
        print("3. Edit note")
        print("4. Delete note")
        print("5. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            text = input("Enter note: ")
            app.add_note(text)

        elif choice == "2":
            app.show_notes()

        elif choice == "3":
            app.show_notes()
            try:
                index = int(input("Enter note number: ")) - 1
                new_text = input("Enter new text: ")
                app.edit_note(index, new_text)
            except ValueError:
                print("Invalid input")

        elif choice == "4":
            app.show_notes()
            try:
                index = int(input("Enter note number: ")) - 1
                app.delete_note(index)
            except ValueError:
                print("Invalid input")

        elif choice == "5":
            break

        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()
