import os
import time
import platform


print("""__________                               
\______   \_______  ____     ____  ______
 |    |  _/\_  __ \/  _ \   /  _ \/  ___/
 |    |   \ |  | \(  <_> ) (  <_> )___ \ 
 |______  / |__|   \____/   \____/____  >
        \/                            \/ """)

time.sleep(1)
print("\n-------------------")
print(" Hello type your username and password ")


def clear_screen():
    os.system('cls' if platform.system() == 'Windows' else 'clear')

while True:
    user_name = input("Username: ")
    pass_user = input("Password: ")

    if user_name == "admin" and pass_user == "12345678":
        clear_screen()
        print("login sucessfull")
        break
    else:
        clear_screen()
        print("incorect username or password\n")