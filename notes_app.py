import os
import platform
import time

def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

def run_notes():
    while True:
        clear_screen()
        print("--- Notes App ---")
        print("1> View Notes")
        print("2> Add a Note")
        print("3> Clear Notes")
        print("q> Back to App List")
        
        note_choice = input("\nEnter your choice: ")

        if note_choice == "1":
            clear_screen()
            print("--- Your Notes ---")
            try:
                with open("notes.txt", "r") as file:
                    content = file.read()
                    if content:
                        print(content)
                    else:
                        print("No notes found. It's empty!")
            except FileNotFoundError:
                print("No notes found. Create a note first!")
            
            input("\nPress Enter to go back...")

        elif note_choice == "2":
            clear_screen()
            print("--- Add a Note ---")
            new_note = input("Write your note here: ")
            with open("notes.txt", "a") as file:
                file.write(f"- {new_note}\n")
            print("\nNote saved successfully!")
            time.sleep(1)

        elif note_choice == "3":
            with open("notes.txt", "w") as file:
                file.write("")
            print("\nAll notes cleared!")
            time.sleep(1)

        elif note_choice.lower() == "q":
            break

        else:
            input("Invalid choice! Press Enter to try again...")