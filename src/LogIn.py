"""
Log in

case 1: log in admin               --> return 1
case 2: log in user                --> return 2
case 3: wrong username or password --> return 3
"""



if __name__ == '__main__':
	input("\033[31mPlease run { __main__.py } in the root directory of this project\033[K")
	quit()


    
from os import path
from datetime import datetime
from .Colour import Colour
from .ClearScreen import clearscreen
from .CommondPath import commond_path



def pyssword(prompt):
    import getpass, sys
    if sys.stdin is not sys.__stdin__:
        pwd = getpass.getpass(prompt)
        return pwd
    else:
        try:
            from msvcrt import getch
            pwd = ""        
            sys.stdout.write(prompt)
            sys.stdout.flush()        
            while True:
                key = ord(getch())
                if key == 13:
                    sys.stdout.write("\n")
                    return pwd
                if key == 8:
                    if len(pwd) > 0:
                        sys.stdout.write("\b" + " " + "\b")                
                        sys.stdout.flush()
                        pwd = pwd[:-1]                    
                else:
                    char = chr(key)
                    sys.stdout.write("*")
                    sys.stdout.flush()                
                    pwd = pwd + char
        except ImportError:
            pwd = getpass.getpass(prompt)
            return pwd



def log_in() -> int:
    user = input("Username: ")
    password = pyssword("Password: ")
    print(Colour.Reset, end = "")
    file_path = path.join('{}'.format(commond_path), 'Account', 'admin.txt')
    f = open(file_path, "r")
    if user == f.readline() [10:-1]:
        if password == (f.readline()) [10:-1]:
            f.close()
            format_time = "%d/%m/%y %H:%M:%S"
            now = datetime.strftime(datetime.now(), format_time)
            list_time = []
            file_path = path.join(commond_path, 'Account', 'admin_login_time.txt')
            f = open(file_path, "r")
            while True:
                line = f.readline() [:-1]
                if line == "":
                    break
                else:
                    list_time.append(line)
            list_time.append(now)
            for i in range(10):
                list_time.append("")
            if list_time [10] != "":
                del list_time [0]
            line = ""
            for i in range(10):
                line += list_time [i] + "\n"
            f.close()
            f = open(file_path, "w")
            f.write(line)
            f.close()
            clearscreen()
            return 1
    file_path = path.join('{}'.format(commond_path), 'Account', 'user.txt')
    f = open(file_path, "r")
    if user == f.readline() [10:-1]:
        if password == (f.readline()) [10:-1]:
            f.close()
            format_time = "%d/%m/%y %H:%M:%S"
            now = datetime.strftime(datetime.now(), format_time)
            list_time = []
            file_path = path.join(commond_path, 'Account', 'user_login_time.txt')
            f = open(file_path, "r")
            while True:
                line = f.readline() [:-1]
                if line == "":
                    break
                else:
                    list_time.append(line)
            list_time.append(now)
            for i in range(10):
                list_time.append("")
            if list_time [10] != "":
                del list_time [0]
            line = ""
            for i in range(10):
                line += list_time [i] + "\n"
            f.close()
            f = open(file_path, "w")
            f.write(line)
            f.close()
            clearscreen()
            return 2
    print(Colour.Red + "USERNAME OR PASSWORD IS INCORRECT" + Colour.Reset)
    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
    clearscreen()
    return 3