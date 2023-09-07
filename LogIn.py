"""
Log in

case 1: log in admin               --> return 1
case 2: log in user                --> return 2
case 3: wrong username or password --> return 0
"""



from getpass import getpass
from pathlib import Path
from Colour import Colour
from ClearScreen import clearscreen



def log_in():
    user = input("Username: ")
    password = getpass("Password: ")
    dir_path = Path("Data", "Account")
    file_name = "admin.txt"
    file_path = dir_path.joinpath(file_name)
    f = open(file_path, "r")
    if user == f.readline() [10:-1]:
        if password == (f.readline()) [10:]:
            f.close()
            clearscreen()
            return 1
    file_name = "user.txt"
    file_path = dir_path.joinpath(file_name)
    f = open(file_path, "r")
    if user == f.readline() [10:-1]:
        if password == (f.readline()) [10:]:
            f.close()
            clearscreen()
            return 2
    print(Colour.Red + "USERNAME OR PASSWORD IS IN CORRECT" + Colour.Reset)
    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
    clearscreen()
    return 0