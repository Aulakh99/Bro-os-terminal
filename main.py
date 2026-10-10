import login
import calculator
import os
import platform
import time
import calendar
from datetime import date
import notes_app





def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

while True:
    clear_screen()
    print("Loding...")
    clear_screen()
    time.sleep(1)
    print("-----App List-----")
    print("\n1> Notes    2> Calendar    3> Calculator")
    print("------------------")
    print("Type shutdown to poweroff")


    print("--------------------------")
    user_input = input("\nEnter the number: ")

    if user_input == "1":
        clear_screen()
        notes_app.run_notes()
        user_exit = input("\nPress 'q' to open App List: ")
        if user_exit.lower() == "q":
            continue

    elif user_input == "2":
        clear_screen()
        print("Loding...")
        time.sleep(1)
        print("--- Calendar App ---") #title
        year = 2026
        print(calendar.calendar(year))

        today = date.today()
        print("Today's date is:", today)

        user_exit = input("\nPress 'q' to open App List: ")
        if user_exit.lower() == "q":
            continue

    elif user_input == "3":
        clear_screen()
        calculator.run_calculator()
        
        user_exit = input("\nPress 'q' to open App List: ")
        if user_exit.lower() == "q":
            continue

    elif user_input == "shutdown":
        clear_screen()
        time.sleep(1)

        print("shuting down......")
        time.sleep(3)
        break


    else:
        input("Invalid choice! Press Enter to try again...")
    



