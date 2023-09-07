"""
Log in

case 1: log in admin               --> return 1
case 2: log in user                --> return 2
case 3: wrong username or password --> return 3
"""



from os import path
from Colour import Colour
from ClearScreen import clearscreen
from CommondPath import commond_path



def log_in():
    user = input("Username: ")
    password = input("Password: \033[8m\033[47m")
    print(Colour.Reset, end = "")
    dir_path = path.join('{}'.format(commond_path), 'Data', 'Account')
    file_path = path.join('{}'.format(dir_path),'admin.txt')
    f = open(file_path, "r")
    if user == f.readline() [10:-1]:
        if password == (f.readline()) [10:-1]:
            f.close()
            clearscreen()
            return 1
    dir_path = path.join('{}'.format(commond_path), 'Data', 'Account')
    file_path = path.join('{}'.format(dir_path),'user.txt')
    f = open(file_path, "r")
    if user == f.readline() [10:-1]:
        if password == (f.readline()) [10:-1]:
            f.close()
            clearscreen()
            return 2
    print(Colour.Red + "USERNAME OR PASSWORD IS IN CORRECT" + Colour.Reset)
    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
    clearscreen()
    return 3