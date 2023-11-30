"""detail in admin_stage.txt"""



if __name__ == '__main__':
	input("\033[31mPlease run { __main__.py } in the root directory of this project\033[K")
	quit()



from random import shuffle
from os import path, rename, rmdir, remove, mkdir
from time import sleep
from datetime import datetime, timedelta
from .CommondPath import commond_path
from .ClearScreen import clearscreen
from .Colour import Colour
from .Seatingplan import print_plan
from .UpdateDatetimeAll import update_status
from .According import filmname_accord, housename_accord, ticket_accord
from .Resetsystem import reset_sys



def file_name_include(str_input: str) -> bool:
    for i in range(len(str_input)):
        if str_input [i] == "\\" or str_input [i] == "/"  or str_input [i] == ":" or str_input [i] == "*" or str_input [i] == "?" or str_input [i] == "\""  or str_input [i] == "<" or str_input [i] == ">" or str_input [i] == "|":
            return False
    return True



def file_name_include_ascii(str_input: str) -> bool:
    for i in range(len(str_input)):
        if ord(str_input [i]):
            if ord(str_input [i]) >= 127 or ord(str_input [i]) <= 31:
                return False
    return True



def input_int_check(output: str, choose) -> int:
    str_input: str = input(output)
    if str_input.isdecimal() and int(str_input) != 0 and int(str_input) <= choose:
        return int(str_input)
    else:
        print(Colour.Reset + Colour.Red + "YOUR INPUT IS INCORRECT" + Colour.Reset)
        input(Colour.Reset + Colour.Yellow + "PRESS ENTER TO RETRY" + Colour.Reset)
        return 0
    


def eng_to_int(strinput: str) -> int:
    bigrow = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    strinput = strinput.upper()
    num = 0
    i = 0
    while i < len(strinput):
        error = 1
        for j in range(1, 27):
            if strinput [i] == bigrow [j - 1]:
                num = num * 26 + j
                error = 0
        if error == 0:
            i += 1
        else:
            i = len(strinput)
    if error == 1:
        return -1
    else:
        return (num - 1)
    


def int_to_eng(a) -> str:
    bigrow = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    strrow = ""
    if a > 25:
        while True:
            b = int(a / 26)
            c = a % 26
            if b > 26:
                strrow = bigrow[c] + strrow
                a = b - 1
            else:
                strrow = bigrow[c] + strrow
                strrow = bigrow[b - 1] + strrow
                break
    else:
        strrow = bigrow[a] + strrow
    return strrow



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
































def print_1() -> int:
    print("""{}ADMIN MENU{}

1 <-- Account
2 <-- House
3 <-- Film
4 <-- Showing
5 <-- Reset system
6 <-- Shut down
7 <-- Log out

""".format(Colour.Underline, Colour.Reset))
    return 7



def print_101() -> int:
    print("""{}Account{}
          
1 <-- User
2 <-- Admin
3 <-- Go back
          
""".format(Colour.Underline, Colour.Reset))
    return 3



def print_102() -> int:
    print("{}User Account{}".format(Colour.Underline, Colour.Reset))
    print("")
    file_path = path.join('{}'.format(commond_path), 'Account', 'user.txt')
    f = open(file_path, "r")
    print(f.readline() [:-1])
    print(f.readline() [:-1])
    f.close()
    print("")
    print("""1 <-- Change username
2 <-- Change password
3 <-- View pervious login time
4 <-- Go back

""")
    return 4
    


def print_103() -> None:
    print("{}User username{}".format(Colour.Underline, Colour.Reset))
    print("")
    file_path = path.join('{}'.format(commond_path), 'Account', 'user.txt')
    f = open(file_path, "r")
    print(f.readline() [:-1])
    f.close()
    print("New username: ", end = "")



def print_104() -> None:
    print("{}User password{}".format(Colour.Underline, Colour.Reset))
    print("")
    file_path = path.join('{}'.format(commond_path), 'Account', 'user.txt')
    f = open(file_path, "r")
    f.readline()
    print(f.readline() [:-1])
    f.close()
    print("New password: ", end = "")



def print_105() -> int:
    print("{}Admin Account{}".format(Colour.Underline, Colour.Reset))
    print("")
    file_path = path.join('{}'.format(commond_path), 'Account', 'admin.txt')
    f = open(file_path, "r")
    print(f.readline() [:-1])
    print(f.readline() [:-1])
    f.close()
    print("")
    print("""1 <-- Change username
2 <-- Change password
3 <-- View pervious login time
4 <-- Go back

""")
    return 4



def print_106() -> None:
    print("{}Admin username{}".format(Colour.Underline, Colour.Reset))
    print("")
    file_path = path.join('{}'.format(commond_path), 'Account', 'admin.txt')
    f = open(file_path, "r")
    print(f.readline() [:-1])
    f.close()
    print("New username: ", end = "")



def print_107() -> None:
    print("{}Admin password{}".format(Colour.Underline, Colour.Reset))
    print("")
    file_path = path.join('{}'.format(commond_path), 'Account', 'admin.txt')
    f = open(file_path, "r")
    f.readline()
    print(f.readline() [:-1])
    f.close()
    print("New password: ", end = "")



def print_108() -> None:
    list_time = []
    file_path = path.join(commond_path, 'Account', 'user_login_time.txt')
    f = open(file_path, "r")
    while True:
        line = f.readline() [:-1]
        if line == "":
            break
        else:
            list_time.append(line)
    print(Colour.Underline + "Login time of user" + Colour.Reset)
    print("")
    for i in list_time:
        print(i)
    print("")
    print("1 <-- Go back")
    print("")
    return 1



def print_109() -> None:
    list_time = []
    file_path = path.join(commond_path, 'Account', 'admin_login_time.txt')
    f = open(file_path, "r")
    while True:
        line = f.readline() [:-1]
        if line == "":
            break
        else:
            list_time.append(line)
    print(Colour.Underline + "Login time of admin" + Colour.Reset)
    print("")
    for i in list_time:
        print(i)
    print("")
    print("1 <-- Go back")
    print("")
    return 1



def print_201() -> int:
    print("{}House{}".format(Colour.Underline, Colour.Reset))
    print("")
    file_path = path.join('{}'.format(commond_path), 'House', 'housename.txt')
    f = open(file_path, "r")
    house = int(f.readline() [:-1])
    housename = []
    for i in range(house):
        housename.append(f.readline() [:-1])
    f.close()
    len_house = len(str(house + 2))
    if house != 0:
        for i in range(house):
            print("{:<{}} <-- {}".format(i + 1, len_house, housename [i]))
        print("{:<{}} <-- Create a new house".format(i + 2, len_house))
        print("{:<{}} <-- Go back".format(i + 3, len_house))
        print("")
        return i + 3
    else:
        print("1 <-- Create a new house")
        print("2 <-- Go back")
        print("")
        return 2



def print_202(house: str) -> int:
    print_plan("", house, -1, -1, 1)
    print(Colour.Underline + "Status of seats" + Colour.Reset + ":")
    print(Colour.Green + "O" + Colour.Reset + " <-> Available seats")
    print(Colour.Blue + "\ua554" + Colour.Reset + " <-> Unavailable seats")
    print("""
1 <-- Change the status of a seats
2 <-- Rename the house
3 <-- {}\u26a0{}{}Delete the house{}{}\u26a0{}
4 <-- Go back

""".format(Colour.Red, Colour.Reset, Colour.Underline, Colour.Reset, Colour.Red, Colour.Reset))
    return 4



def print_203(house: str) -> None:
    print_plan("", house, -1, -1, 1)
    print(Colour.Underline + "Status of seats" + Colour.Reset + ":")
    print(Colour.Green + "O" + Colour.Reset + " <-> Available seats")
    print(Colour.Blue + "\ua554" + Colour.Reset + " <-> Unavailable seats")
    print("")
    print("Enter exit --> exit")
    print("")



def print_204(house, row_highlight, column_highlight) -> int:
    print_plan("", house, row_highlight, column_highlight, 1)
    row_string = int_to_eng(row_highlight)
    file_path = path.join('{}'.format(commond_path), 'House', '{}'.format(house), 'houseplan.txt')
    f = open(file_path, "r")
    for i in range(row_highlight):
        f.readline()
    seat = f.readline() [:-1]
    seat = seat [column_highlight]
    f.close()
    print(Colour.Underline + "Status of seats" + Colour.Reset + ":")
    print(Colour.Green + "O" + Colour.Reset + " <-> Available seats")
    print(Colour.Blue + "\ua554" + Colour.Reset + " <-> Unavailable seats")
    print("")
    if int(seat) != 0:
        print("1 <-- Change {}{} to {}O{}".format(row_string, column_highlight + 1, Colour.Green, Colour.Reset))
    else:
        print("1 <-- Change {}{} to {}\ua554{}".format(row_string, column_highlight + 1, Colour.Blue, Colour.Reset))
    print("2 <-- Go back")
    print("")
    return int(seat)



def print_205(house) -> None:
    print("{}{} Renaming{}".format(Colour.Underline, house, Colour.Reset))
    print("")
    print("Current name: {}".format(house [6:]))
    print("New name: ", end = "")



def print_206(house) -> str:
    bigrow = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    smallrow = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    code = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T" ,"Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
    print(Colour.Red + "\u26a0\u26a0\u26a0All data of { " + house + " } will be delete and impossible to be recovery!\u26a0\u26a0\u26a0" + Colour.Reset)
    num_check = 0
    small_check = 0
    big_check = 0
    while num_check == 0 or small_check == 0 or big_check == 0:
        num_check = 0
        small_check = 0
        big_check = 0
        shuffle(code)
        for i in range(10):
            for j in range(26):
                if code [i] == bigrow [j]:
                    big_check = 1
                elif code [i] == smallrow [j]:
                    small_check = 1
            if code [i].isdecimal():
                num_check = 1
    temp = ""
    for i in range(10):
        temp = temp + code [i]
    print("Enter the security code to delete { " + house + " }.")
    print("")
    print("Security code: " + temp)
    return temp



def print_301() -> int:
    print(Colour.Underline + "Film" + Colour.Reset)
    print("")
    file_path = path.join(commond_path, 'Film', 'filmname.txt')
    f = open(file_path, "r")
    film = int(f.readline() [:-1])
    filmname = []
    for i in range(film):
        filmname.append(f.readline() [:-1])
    f.close()
    len_film = len(str(film + 2))
    if film != 0:
        for i in range(film):
            print("{:<{}} <-- {}".format(i + 1, len_film, filmname [i]))
        print("{:<{}} <-- Film addition".format(i + 2, len_film))
        print("{:<{}} <-- Go back".format(i + 3, len_film))
        print("")
        return i + 3
    else:
        print("1 <-- Film addition")
        print("2 <-- Go back")
        print("")
        return 2



def print_302(filmname) -> int:
    print(Colour.Underline + "{}".format(filmname) + Colour.Reset)
    print("")
    print("Name      : {}".format(filmname))
    commond_file_path = path.join(commond_path, 'Film', filmname)
    file_path = path.join(commond_file_path, 'timelength.txt')
    f = open(file_path, "r")
    timelength = int(f.readline())
    f.close()
    file_path = path.join(commond_file_path, 'rating.txt')
    f = open(file_path, "r")
    rating = f.readline()
    f.close()
    file_path = path.join(commond_file_path, 'language.txt')
    f = open(file_path, "r")
    language_count = int(f.readline() [:-1])
    language = []
    for i in range(language_count):
        language.append(f.readline() [:-1])
    f.close()
    file_path = path.join(commond_file_path, 'dimension.txt')
    f = open(file_path, "r")
    dimension_count = int(f.readline() [:-1])
    dimension = []
    for i in range(dimension_count):
        dimension.append(f.readline() [:-1])
    f.close()
    file_path = path.join(commond_file_path, 'price.txt')
    f = open(file_path, "r")
    price_count = dimension_count
    price = []
    for i in range(price_count):
        price.append(f.readline() [:-1])
    f.close()
    file_path = path.join(commond_file_path, 'st_price.txt')
    f = open(file_path, "r")
    st_price_count = dimension_count
    st_price = []
    for i in range(price_count):
        st_price.append(f.readline() [:-1])
    f.close()
    len_dimension_price = []
    for i in range(dimension_count):
        if len(dimension [i]) >= len(price [i]) + 1:
            if len(dimension [i]) >= len(st_price [i]) + 1:
                len_dimension_price.append(len(dimension [i]))
            else:
                len_dimension_price.append(len(st_price [i]) + 1)
        else:
            if len(price [i]) >= len(st_price [i]) + 1:
                len_dimension_price.append(len(price [i]) + 1)
            else:
                len_dimension_price.append(len(st_price [i]) + 1)
    print("Timelength   : {} minutes".format(str(timelength)))
    print("Rating       : {}".format(rating))
    print("Language     : ", end = "")
    for i in range(language_count):
        if i != 0:
            print(", ", end = "")
        print(language [i], end = "")
    print("")
    print("Dimension    : ", end = "")
    for i in range(dimension_count):
        if i != 0:
            print(", ", end = "")
        print("{:<{}}".format(dimension [i], len_dimension_price [i]), end = "")
    print("")
    print("Price        : ", end = "")
    for i in range(price_count):
        if i != 0:
            print(", ", end = "")
        print("{:<{}}".format("$" + price [i], len_dimension_price [i]), end = "")
    print("")
    print("Student price: ", end = "")
    for i in range(st_price_count):
        if i != 0:
            print(", ", end = "")
        print("{:<{}}".format("$" + st_price [i], len_dimension_price [i]), end = "")
    print("")
    print("""1 <-- Rename
2 <-- Change timelength
3 <-- Change rating
4 <-- Change language
5 <-- Change dimension
6 <-- Change price
7 <-- {}\u26a0{}{}Delete the film{}{}\u26a0{}
8 <-- Go back""".format(Colour.Red, Colour.Reset, Colour.Underline, Colour.Reset, Colour.Red, Colour.Reset))
    print("")
    return 8



def print_305(filmname) -> int:
    print(Colour.Underline + filmname + Colour.Reset)
    print("")
    rating = ["I", "IIA", "IIB", "III"]
    file_path = path.join(commond_path, 'Film', filmname, 'rating.txt')
    f = open(file_path, "r")
    c_rating = f.readline()
    f.close()
    for i in range(3):
        if rating [i] == c_rating:
            temp = rating [i]
            rating [i] = rating [i + 1]
            rating [i + 1] = temp
    print("""Current rating: {}

1 <-- Change to {}
2 <-- Change to {}
3 <-- Change to {}
4 <-- Go back""".format(c_rating, rating [0], rating [1], rating[2]))
    print("")
    return 4



def print_306(filmname) -> int:
    print(Colour.Underline + filmname + Colour.Reset)
    print("")
    file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
    f = open(file_path, "r")
    language_count = int(f.readline() [:-1])
    language = []
    for i in range(language_count):
        language.append(f.readline() [:-1])
    f.close()
    print("Current language : ", end = "")
    for i in range(language_count):
        if i != 0:
            print(", ", end = "")
        print(language [i], end = "")
    print("")
    print("")
    print("""1 <-- Language addition
2 <-- Language deletion
3 <-- Go back""")
    print("")
    return 3



def print_307(filmname) -> None:
    print(Colour.Underline + filmname + Colour.Reset)
    print("")
    file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
    f = open(file_path, "r")
    language_count = int(f.readline() [:-1])
    language = []
    for i in range(language_count):
        language.append(f.readline() [:-1])
    f.close()
    print("Current language : ", end = "")
    for i in range(language_count):
        if i != 0:
            print(", ", end = "")
        print(language [i], end = "")
    print("")



def print_308(filmname) -> int:
    print(Colour.Underline + filmname + Colour.Reset)
    print("")
    file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
    f = open(file_path, "r")
    language_count = int(f.readline() [:-1])
    language = []
    for i in range(language_count):
        language.append(f.readline() [:-1])
    f.close()
    print("Current language : ", end = "")
    for i in range(language_count):
        if i != 0:
            print(", ", end = "")
        print(language [i], end = "")
    print("")
    print("")
    len_language_count = len(str(language_count))
    if language_count == 1:
        print("There is only one language for this film.")
        print("1 <-- Go back")
        print("")
        return 1
    for i in range(language_count):
        print("{:<{}} <-- Delete {}".format(i + 1, len_language_count, language [i]))
    print("{:<{}} <-- Go back".format(i + 2, len_language_count))
    print("")
    return i + 2



def print_309(filmname) -> int:
    print(Colour.Underline + filmname + Colour.Reset)
    print("")
    file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
    f = open(file_path, "r")
    dimension_count = int(f.readline() [:-1])
    dimension = []
    for i in range(dimension_count):
        dimension.append(f.readline() [:-1])
    f.close()
    print("Current dimension : ", end = "")
    for i in range(dimension_count):
        if i != 0:
            print(", ", end = "")
        print(dimension [i], end = "")
    print("")
    print("")
    print("""1 <-- Dimension addition
2 <-- Dimension deletion
3 <-- Go back""")
    print("")
    return 3



def print_310(filmname) -> None:
    print(Colour.Underline + filmname + Colour.Reset)
    print("")
    file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
    f = open(file_path, "r")
    dimension_count = int(f.readline() [:-1])
    dimension = []
    for i in range(dimension_count):
        dimension.append(f.readline() [:-1])
    f.close()
    print("Current dimension : ", end = "")
    for i in range(dimension_count):
        if i != 0:
            print(", ", end = "")
        print(dimension [i], end = "")
    print("")



def print_311(filmname) -> int:
    print(Colour.Underline + filmname + Colour.Reset)
    print("")
    file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
    f = open(file_path, "r")
    dimension_count = int(f.readline() [:-1])
    dimension = []
    for i in range(dimension_count):
        dimension.append(f.readline() [:-1])
    f.close()
    print("Current dimension : ", end = "")
    for i in range(dimension_count):
        if i != 0:
            print(", ", end = "")
        print(dimension [i], end = "")
    print("")
    print("")
    len_dimension_count = len(str(dimension_count + 1))
    if dimension_count == 1:
        print("There is only one dimension for this film.")
        print("1 <-- Go back")
        print("")
        return 1
    for i in range(dimension_count):
        print("{:<{}} <-- Delete {}".format(i + 1, len_dimension_count, dimension [i]))
    print("{:<{}} <-- Go back".format(i + 2, len_dimension_count))
    print("")
    return i + 2



def print_313(filmname) -> str:
    bigrow = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    smallrow = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    code = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T" ,"Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
    print(Colour.Red + "\u26a0\u26a0\u26a0All data of { " + filmname + " } will be delete and impossible to be recovery!\u26a0\u26a0\u26a0" + Colour.Reset)
    num_check = 0
    small_check = 0
    big_check = 0
    while num_check == 0 or small_check == 0 or big_check == 0:
        num_check = 0
        small_check = 0
        big_check = 0
        shuffle(code)
        for i in range(10):
            for j in range(26):
                if code [i] == bigrow [j]:
                    big_check = 1
                elif code [i] == smallrow [j]:
                    small_check = 1
            if code [i].isdecimal():
                num_check = 1
    temp = ""
    for i in range(10):
        temp = temp + code [i]
    print("Enter the security code to delete { " + filmname + " }.")
    print("")
    print("Security code: " + temp)
    return temp



def print_401() -> int:
    print(Colour.Underline + "Showing" + Colour.Reset)
    print("")
    temp = 0
    file_path = path.join(commond_path, 'House', 'housename.txt')
    f = open(file_path, "r")
    if f.readline() [:-1] == "0":
        temp += 1
    file_path = path.join(commond_path, 'Film', 'filmname.txt')
    f = open(file_path, "r")
    if f.readline() [:-1] == "0":
        temp += 2
    if temp == 0:
        print("""1 <-- Filter with film
2 <-- Filter with house
3 <-- Filter with status
4 <-- Search showing
5 <-- Create showing 
6 <-- Go back""")
        print("")
        return 6
    elif temp == 1:
        print("""There is no houses in the system.
1 <-- Go back""")
        print("")
        return 1
    elif temp == 2:
        print("""There is no films in the system.
1 <-- Go back""")
        print("")
        return 1
    else:
        print("""There is no houses and films in the system.
1 <-- Go back""")
        print("")
        return 1



def print_402() -> int:
    print(Colour.Underline + "Showing filtering" + Colour.Reset)
    print("")
    file_path = path.join(commond_path, 'Film', 'filmname.txt')
    f = open(file_path, "r")
    count_film = int(f.readline() [:-1])
    len_count_film = len(str(count_film + 1))
    for i in range(count_film):
        print("{:<{}} <-- Filter with {}{}{}".format(i + 1, len_count_film, "{ ", f.readline() [:-1], " }"))
    f.close()
    print("{:<{}} <-- Go back".format(i + 2, len_count_film))
    print("")
    return i + 2



def print_403(filmname) -> int:
    print(Colour.Underline + "Showing filtering" + Colour.Reset)
    print("")
    print("Film: " + filmname)
    print("")
    file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
    f = open(file_path, "r")
    count_dimension = int(f.readline() [:-1])
    len_count_dimension = len(str(count_dimension + 1))
    for i in range(count_dimension):
        print("{:<{}} <-- Filter with {}".format(i + 1, len_count_dimension, f.readline() [:-1]))
    f.close()
    print("{:<{}} <-- Go back".format(i + 2, len_count_dimension))
    print("")
    return i + 2



def print_404(filmname, dimension) -> int:
    print(Colour.Underline + "Showing filtering" + Colour.Reset)
    print("")
    print("Film     : " + filmname)
    print("Dimension: " + dimension)
    print("")
    file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
    f = open(file_path, "r")
    count_language = int(f.readline() [:-1])
    len_count_language = len(str(count_language + 1))
    for i in range(count_language):
        print("{:<{}} <-- Filter with {}".format(i + 1, len_count_language, f.readline() [:-1]))
    f.close()
    print("{:<{}} <-- Go back".format(i + 2, len_count_language))
    print("")
    return i + 2



def print_405(filmname, dimension, language) -> int:
    print(Colour.Underline + "Showing filtering" + Colour.Reset)
    print("")
    print("Film     : " + filmname)
    print("Dimension: " + dimension)
    print("Language : " + language)
    print("")
    print("1 <-- Ended showings")
    print("2 <-- Playing showings")
    print("3 <-- Upcoming showings")
    print("4 <-- Go back")
    print("")
    return 4



def print_406(filmname, dimension, language, time) -> int:
    update_status()
    print(Colour.Underline + "Showing filtered" + Colour.Reset)
    print("")
    print("Film     : " + filmname)
    print("Dimension: " + dimension)
    print("Language : " + language)
    if time == "previous":
        print("Status   : Ended")
    elif time == "playing":
        print("Status   : Playing")
    else:
        print("Status   : Upcoming")
    print("")
    if not path.exists(path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showing.txt')):
        print("There is no showing matching condition.")
        print("1 <-- Go back")
        print("")
        return 1
    file_path = path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showingnum.txt')
    f = open(file_path, "r")
    sum_showing = int(f.readline())
    f.close()
    count_showing = 0
    showing = []
    file_path = path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showing.txt')
    f = open(file_path, "r")
    for i in range(sum_showing):
        if f.readline() [:-1] == time:
            count_showing += 1
            showing.append(f.readline() [:-1])
        else:
            f.readline()
    f.close()
    if count_showing == 0:
        print("There is no showing matching condition.")
        print("1 <-- Go back")
        print("")
        return 1
    else:
        format_time = "%d/%m/%y %H:%M:%S"
        len_count_showing = len(str(count_showing + 1))
        for i in range(count_showing):
            print("{:<{}} <-- {}".format(i + 1, len_count_showing, showing [i]))
            file_path = path.join(commond_path, 'Showing', showing [i], 'house.txt')
            f = open(file_path, "r")
            print("{:<{}}     House         : {}".format(" ", len_count_showing, f.readline()))
            f.close()
            file_path = path.join('{}'.format(commond_path), 'Showing', showing [i], 'houseplan.txt')
            f = open(file_path)
            row = 0
            avail_count = 0
            while True:
                temp = f.readline() [:-1]
                if temp == "":
                    break
                else:
                    column = len(temp)
                    row += 1
                    for k in range(column):
                        if temp [k] == "0":
                            avail_count += 1
            all_seat = column * row
            f.close()
            if avail_count == 0:
                haha = Colour.Red
            elif avail_count / all_seat <= 0.5:
                haha = Colour.Yellow
            else:
                haha = Colour.Green
            print("{:<{}}     Available seat: {}{}{}/{}".format(" ", len_count_showing, haha, avail_count, Colour.Reset, all_seat))
            file_path = path.join(commond_path, 'Showing', showing [i], 'starttime.txt')
            f = open(file_path, "r")
            starttime = datetime.strptime(f.readline(), format_time)
            f.close()
            file_path = path.join(commond_path, 'Film', filmname, 'timelength.txt')
            f = open(file_path, "r")
            endtime = starttime + timedelta(minutes = int(f.readline()))
            f.close()
            print("{:<{}}     Time          : {} - {}".format(" ", len_count_showing, starttime.strftime(format_time), endtime.strftime(format_time)))
        print("{} <-- Go back".format(i + 2))
        print("")
        return i + 2



def print_407() -> int:
    print(Colour.Underline + "Showing filtering" + Colour.Reset)
    print("")
    file_path = path.join(commond_path, 'House', 'housename.txt')
    f = open(file_path, "r")
    count_house = int(f.readline() [:-1])
    len_count_house = len(str(count_house + 1))
    for i in range(count_house):
        print("{:<{}} <-- Filter with {}{}{}".format(i + 1, len_count_house, "{ ", f.readline() [:-1], " }"))
    f.close()
    print("{:<{}} <-- Go back".format(i + 2, len_count_house))
    print("")
    return i + 2



def print_408(house) -> int:
    print(Colour.Underline + "Showing filtering" + Colour.Reset)
    print("")
    print("House: " + house)
    print("")
    print("1 <-- Ended showings")
    print("2 <-- Playing showings")
    print("3 <-- Upcoming showings")
    print("4 <-- Go back")
    print("")
    return 4



def print_409(house, time) -> int:
    update_status()
    print(Colour.Underline + "Showing filtered" + Colour.Reset)
    print("")
    print("House : " + house)
    if time == "previous":
        print("Status   : Ended")
    elif time == "playing":
        print("Status   : Playing")
    else:
        print("Status   : Upcoming")
    print("")
    if not path.exists(path.join(commond_path, 'Showing', '__House information', house, 'Showing.txt')):
        print("There is no showing matching condition.")
        print("1 <-- Go back")
        print("")
        return 1
    file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showingnum.txt')
    f = open(file_path, "r")
    sum_showing = int(f.readline())
    f.close()
    count_showing = 0
    showing = []
    file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showing.txt')
    f = open(file_path, "r")
    for i in range(sum_showing):
        if f.readline() [:-1] == time:
            count_showing += 1
            showing.append(f.readline() [:-1])
        else:
            f.readline()
    f.close()
    if count_showing == 0:
        print("There is no showing matching condition.")
        print("1 <-- Go back")
        print("")
        return 1
    else:
        format_time = "%d/%m/%y %H:%M:%S"
        len_count_showing = len(str(count_showing + 1))
        for i in range(count_showing):
            print("{:<{}} <-- {}".format(i + 1, len_count_showing, showing [i]))
            file_path = path.join(commond_path, 'Showing', showing [i], 'film.txt')
            f = open(file_path, "r")
            filmname = f.readline() [:-1]
            print("{:<{}}     Film          : {}".format(" ", len_count_showing, filmname))
            print("{:<{}}     Dimension     : {}".format(" ", len_count_showing, f.readline() [:-1]))
            print("{:<{}}     Language      : {}".format(" ", len_count_showing, f.readline() [:-1]))
            f.close()
            file_path = path.join('{}'.format(commond_path), 'Showing', showing [i], 'houseplan.txt')
            f = open(file_path)
            row = 0
            avail_count = 0
            while True:
                temp = f.readline() [:-1]
                if temp == "":
                    break
                else:
                    column = len(temp)
                    row += 1
                    for k in range(column):
                        if temp [k] == "0":
                            avail_count += 1
            all_seat = column * row
            f.close()
            if avail_count == 0:
                haha = Colour.Red
            elif avail_count / all_seat <= 0.5:
                haha = Colour.Yellow
            else:
                haha = Colour.Green
            print("{:<{}}     Available seat: {}{}{}/{}".format(" ", len_count_showing, haha, avail_count, Colour.Reset, all_seat))
            file_path = path.join(commond_path, 'Showing', showing [i], 'starttime.txt')
            f = open(file_path, "r")
            starttime = datetime.strptime(f.readline(), format_time)
            f.close()
            file_path = path.join(commond_path, 'Film', filmname, 'timelength.txt')
            f = open(file_path, "r")
            endtime = starttime + timedelta(minutes = int(f.readline()))
            f.close()
            print("{:<{}}     Time          : {} - {}".format(" ", len_count_showing, starttime.strftime(format_time), endtime.strftime(format_time)))
        print("{} <-- Go back".format(i + 2))
        print("")
        return i + 2



def print_410() -> int:
    print(Colour.Underline + "Showing filtering" + Colour.Reset)
    print("")
    print("1 <-- Ended")
    print("2 <-- Playing")
    print("3 <-- Upcoming")
    print("4 <-- Go back")
    print("")
    return 4



def print_411(time) -> int:
    update_status()
    print(Colour.Underline + "Showing filtering" + Colour.Reset)
    print("")
    print("Status: " + time)
    print("")
    file_path = path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt')
    f = open(file_path, "r")
    sum_showing = int(f.readline())
    f.close()
    count_showing = 0
    showing = []
    file_path = path.join(commond_path, 'Showing', '__Time information', 'Showing.txt')
    f = open(file_path, "r")
    for i in range(sum_showing):
        if f.readline() [:-1] == time:
            count_showing += 1
            showing.append(f.readline() [:-1])
        else:
            f.readline()
    f.close()
    if count_showing == 0:
        print("There is no showing matching condition.")
        print("1 <-- Go back")
        print("")
        return 1
    else:
        format_time = "%d/%m/%y %H:%M:%S"
        len_count_showing = len(str(count_showing + 1))
        for i in range(count_showing):
            print("{:<{}} <-- {}".format(i + 1, len_count_showing, showing [i]))
            file_path = path.join(commond_path, 'Showing', showing [i], 'film.txt')
            f = open(file_path, "r")
            filmname = f.readline() [:-1]
            print("{:<{}}     Film          : {}".format(" ", len_count_showing, filmname))
            print("{:<{}}     Dimension     : {}".format(" ", len_count_showing, f.readline() [:-1]))
            print("{:<{}}     Language      : {}".format(" ", len_count_showing, f.readline() [:-1]))
            f.close()
            file_path = path.join(commond_path, 'Showing', showing [i], 'house.txt')
            f = open(file_path, "r")
            print("{:<{}}     House         : {}".format(" ", len_count_showing, f.readline()))
            f.close()
            file_path = path.join(commond_path, 'Showing', showing [i], 'houseplan.txt')
            f = open(file_path, "r")
            row = 0
            avail_count = 0
            while True:
                temp = f.readline() [:-1]
                if temp == "":
                    break
                else:
                    column = len(temp)
                    row += 1
                    for k in range(column):
                        if temp [k] == "0":
                            avail_count += 1
            all_seat = column * row
            f.close()
            if avail_count == 0:
                haha = Colour.Red
            elif avail_count / all_seat <= 0.5:
                haha = Colour.Yellow
            else:
                haha = Colour.Green
            print("{:<{}}     Available seat: {}{}{}/{}".format(" ", len_count_showing, haha, avail_count, Colour.Reset, all_seat))
            file_path = path.join(commond_path, 'Showing', showing [i], 'starttime.txt')
            f = open(file_path, "r")
            starttime = datetime.strptime(f.readline(), format_time)
            f.close()
            file_path = path.join(commond_path, 'Film', filmname, 'timelength.txt')
            f = open(file_path, "r")
            endtime = starttime + timedelta(minutes = int(f.readline()))
            f.close()
            print("{:<{}}     Time          : {} - {}".format(" ", len_count_showing, starttime.strftime(format_time), endtime.strftime(format_time)))
        print("{} <-- Go back".format(i + 2))
        print("")
        return i + 2



def print_412() -> None:
    print(Colour.Underline + "Search showing" + Colour.Reset)
    print("")
    print("Showings: ")
    file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
    f = open(file_path, "r")
    count_showing = int(f.readline())
    f.close()
    file_path = path.join(commond_path, 'Showing', 'Showing.txt')
    f = open(file_path, "r")
    showing = []
    for i in range(count_showing):
        showing.append(f.readline() [:-1])
    f.close()
    missshowing = []
    file_path = path.join(commond_path, 'Showing', 'Missshowing.txt')
    f = open(file_path, "r")
    while True:
        line = f.readline() [:-1]
        if line == "":
            break
        else:
            count_showing += 1
            missshowing.append(line)
            showing.append(line)
    f.close()
    len_count_showing = len(str(count_showing + 1))
    for i in range(count_showing):
        for j in range(i + 1, count_showing):
            if showing [j - 1] >= showing [j]:
                temp = showing [j - 1]
                showing [j - 1] = showing [j]
                showing [j] = temp
    if count_showing != 0:
        for i in range(count_showing):
            error = 0
            for j in missshowing:
                if showing [i] == j:
                    error = 1
                    print("{:<{}} <-- {} (Deleted)".format(i + 1, len_count_showing, showing [i]))
            if error == 0:
                print("{:<{}} <-- {}".format(i + 1, len_count_showing, showing [i]))
        print("{:<{}} <-- Go back".format(i + 2, len_count_showing))
        print("")
        return i + 2
    else:
        print("There is no showings in the system.")
        print("1 <-- Go back")
        return 1



def print_413(showing) -> int:
    print(Colour.Underline + showing + Colour.Reset)
    print("")
    file_path = path.join(commond_path, 'Showing', showing, 'film.txt')
    f = open(file_path, "r")
    filmname = f.readline() [:-1]
    dimension = f.readline() [:-1]
    language = f.readline() [:-1]
    f.close()
    file_path = path.join(commond_path, 'Showing', showing, 'house.txt')
    f = open(file_path, "r")
    house = f.readline()
    f.close()
    file_path = path.join(commond_path, 'Showing', showing, 'houseplan.txt')
    f = open(file_path, "r")
    row = 0
    avail_count = 0
    while True:
        temp = f.readline() [:-1]
        if temp == "":
            break
        else:
            column = len(temp)
            row += 1
            for k in range(column):
                if temp [k] == "0":
                    avail_count += 1
    all_seat = column * row
    f.close()
    if avail_count == 0:
        haha = Colour.Red
    elif avail_count / all_seat <= 0.5:
        haha = Colour.Yellow
    else:
        haha = Colour.Green
    format_time = "%d/%m/%y %H:%M:%S"
    file_path = path.join(commond_path, 'Showing', showing, 'starttime.txt')
    f = open(file_path, "r")
    starttime = datetime.strptime(f.readline(), format_time)
    f.close()
    file_path = path.join(commond_path, 'Film', filmname, 'timelength.txt')
    f = open(file_path, "r")
    endtime = starttime + timedelta(minutes = int(f.readline()))
    f.close()
    print("Film          : " + filmname)
    print("Dimension     : " + dimension)
    print("Language      : " + language)
    print("House         : " + house)
    print("Available seat: " + haha + str(avail_count) + Colour.Reset + "/" + str(all_seat))
    print("Time          : " + starttime.strftime(format_time) + " - " + endtime.strftime(format_time))
    print("")
    print("1 <-- Change film")
    print("2 <-- Change dimension")
    print("3 <-- Change language")
    print("4 <-- Change start time")
    print("5 <-- Check house and ticket information")
    print("6 <-- Delete showing")
    print("7 <-- Go back")
    print("")
    return 7



def print_414(showing, filmname, dimension, stage) -> int:
    if stage == 0:
        print(Colour.Underline + showing + Colour.Reset)
        print("")
        file_path = path.join(commond_path, 'Showing', showing, 'film.txt')
        f = open(file_path, "r")
        filmname = f.readline() [:-1]
        f.close()
        print("Current film: " + filmname)
        file_path = path.join(commond_path, 'Film', 'filmname.txt')
        f = open(file_path, "r")
        film_list = []
        film_count = int(f.readline() [:-1])
        for i in range(film_count):
            film_list.append(f.readline() [:-1])
            if film_list [i] == filmname:
                film_list [i] = ""
        f.close()
        for i in range(film_count):
            if film_list [i] == "":
                temp = i
        del film_list [temp]
        len_film = len(str(film_count + 1))
        print("")
        if film_count == 0:
            print("There is no other films.")
            print("1 <-- Go back")
            return 1
        for i in range(film_count - 1):
            if film_list [i] != "":
                print("{:<{}} <-- Change to {}".format(i + 1, len_film, film_list [i]))
        print("{:<{}} <-- Go back".format(i + 2, len_film))
        print("")
        return i + 2
    elif stage == 1:   
        print(Colour.Underline + showing + Colour.Reset)
        print("")
        print("Film: " + filmname)
        file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
        f = open(file_path, "r")
        dimension_list = []
        dimension_count = int(f.readline() [:-1])
        for i in range(dimension_count):
            dimension_list.append(f.readline() [:-1])
        f.close()
        len_dimension = len(str(dimension_count + 1))
        print("")
        i = -1
        for i in range(dimension_count):
            if dimension_list [i] != "":
                print("{:<{}} <-- Set dimension {}".format(i + 1, len_dimension, dimension_list [i]))
        print("{:<{}} <-- Go back".format(i + 2, len_dimension))
        print("")
        return i + 2
    else:
        print(Colour.Underline + showing + Colour.Reset)
        print("")
        print("Film:      " + filmname)
        print("Dimension: " + dimension)
        file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
        f = open(file_path, "r")
        language_list = []
        language_count = int(f.readline() [:-1])
        for i in range(language_count):
            language_list.append(f.readline() [:-1])
        f.close()
        len_language = len(str(language_count + 1))
        print("")
        count = 0
        for i in range(language_count):
            if language_list [i] != "":
                count += 1
                print("{:<{}} <-- Set language {}".format(i + 1, len_language, language_list [i]))
        print("{:<{}} <-- Go back".format(i + 2, len_language))
        print("")
        return i + 2



def print_415(showing) -> int:
    file_path = path.join(commond_path, 'Showing', showing, 'film.txt')
    f = open(file_path, "r")
    filmname = f.readline() [:-1]
    dimension = f.readline() [:-1]
    f.close()
    print(Colour.Underline + showing + Colour.Reset)
    print("")
    print("Film: " + filmname)
    file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
    f = open(file_path, "r")
    dimension_list = []
    dimension_count = int(f.readline() [:-1])
    for i in range(dimension_count):
        dimension_list.append(f.readline() [:-1])
    f.close()
    dimension_count2 = dimension_count
    for i in range(dimension_count - 1, -1, -1):
        if dimension_list [i] == dimension:
            del dimension_list [i]
            dimension_count2 -= 1
    len_dimension = len(str(dimension_count + 1))
    print("")
    count = 0
    for i in range(dimension_count2):
        count += 1
        print("{:<{}} <-- Set dimension {}".format(i + 1, len_dimension, dimension_list [i]))
    if count == 0:
        print("There is no other dimensions.")
        print("1 <-- Go back")
        print("")
        return 1
    else:
        print("{:<{}} <-- Go back".format(i + 2, len_dimension))
        print("")
        return i + 2



def print_416(showing) -> int:
    file_path = path.join(commond_path, 'Showing', showing, 'film.txt')
    f = open(file_path, "r")
    filmname = f.readline() [:-1]
    f.readline()
    language = f.readline() [:-1]
    f.close()
    print(Colour.Underline + showing + Colour.Reset)
    print("")
    print("Film: " + filmname)
    file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
    f = open(file_path, "r")
    language_list = []
    language_count = int(f.readline() [:-1])
    for i in range(language_count):
        language_list.append(f.readline() [:-1])
    f.close()
    language_count2 = language_count
    for i in range(language_count - 1, -1, -1):
        if language_list [i] == language:
            del language_list [i]
            language_count2 -= 1
    len_language = len(str(language_count + 1))
    print("")
    count = 0
    for i in range(language_count2):
        count += 1
        print("{:<{}} <-- Set language {}".format(i + 1, len_language, language_list [i]))
    if count == 0:
        print("There is no other languages.")
        print("1 <-- Go back")
        print("")
        return 1
    else:
        print("{:<{}} <-- Go back".format(i + 2, len_language))
        print("")
        return i + 2
    


def print_417(showing) -> None:
    format_time = "%d/%m/%y %H:%M:%S"
    file_path = path.join(commond_path, 'Showing', showing, 'film.txt')
    f = open(file_path, "r")
    filmname = f.readline() [:-1]
    f.close()
    file_path = path.join(commond_path, 'Film', filmname, 'timelength.txt')
    f = open(file_path, "r")
    timelength = int(f.readline())
    f.close()
    file_path = path.join(commond_path, 'Showing', showing, 'starttime.txt')
    f = open(file_path, "r")
    start_time = datetime.strptime(f.readline(), format_time)
    f.close()
    print(Colour.Underline + showing + Colour.Reset)
    print("")
    print("Format             : DD/MM/YY HH:MM:SS")
    print("Time of showing    : " + datetime.strftime(start_time, format_time) + " - " + datetime.strftime(start_time + timedelta(minutes = timelength), format_time))
    print("Time length of film: " + str(timelength) + " minutes")
    print("")
    print("Input \"exit\" to exit")



def print_418(showing) -> int:
    print_plan(showing, "", -1, -1, 0)
    file_path = path.join(commond_path, 'Showing', showing, 'ticket.txt')
    f = open(file_path, "r")
    ticket_count = 0
    ticket = []
    while True:
        temp = f.readline()
        if temp == "":
            break
        else:
            ticket_count += 1
            ticket.append(temp [:-1])
    len_ticket = len(str(ticket_count + 2))
    print("")
    print(Colour.Underline + "Status of seats" + Colour.Reset + ":")
    print(Colour.Green + "O" + Colour.Reset + " <-> Available seats")
    print(Colour.Red + "X" + Colour.Reset + " <-> Sold seats")
    print(Colour.Blue + "\ua554" + Colour.Reset + " <-> Unavailable seats")
    print("")
    count = 0
    for i in range(ticket_count):
        count += 1
        print("{:<{}} <-- Check ticket {}".format(i + 1, len_ticket, ticket [i]))
    if count == 0:
        print("There is no tickets.")
        print("1 <-- Change house")
        print("2 <-- Go back")
        print("")
        return 2
    else:
        print("{:<{}} <-- Change house".format(i + 2, len_ticket))
        print("{:<{}} <-- Go back".format(i + 3, len_ticket))
        print("")
        return i + 3



def print_419(showing) -> int:
    file_path = path.join(commond_path, 'Showing', showing, 'house.txt')
    f = open(file_path, "r")
    house = f.readline()
    f.close()
    file_path = path.join(commond_path, 'House', 'housename.txt')
    f = open(file_path, "r")
    house_count = int(f.readline() [:-1])
    house_list = []
    for i in range(house_count):
        temp = f.readline() [:-1]
        if temp != house:
            house_list.append(temp)
    house_count -= 1
    print(Colour.Underline + showing + Colour.Reset)
    print("")
    print("Current house: ")
    len_house = len(str(house_count + 1))
    count = 0
    for i in range(house_count):
        count += 1
        print("{:<{}} <-- Change house to {}".format(i + 1, len_house, house_list [i]))
    if count == 0:
        print("There is no other houses.")
        print("1 <-- Go back")
        print("")
        return 1
    else:
        print("{:<{}} <-- Go back".format(i + 2, len_house))
        print("")
        return i + 2
    


def print_420(showing, ticket) -> int:
    ticket = ticket [11:-1]
    column = ticket
    while not column.isdecimal():
        column = column [1:]
    column = int(column) - 1
    row = ticket
    for i in range(len(str(column + 1))):
        row = row [:-1]
    row = eng_to_int(row)
    print_plan(showing, "", row, column, 3)
    print("")
    print(Colour.Underline + "Status of seats" + Colour.Reset + ":")
    print(Colour.Green + "O" + Colour.Reset + " <-> Available seats")
    print(Colour.Red + "X" + Colour.Reset + " <-> Sold seats")
    print(Colour.Blue + "\ua554" + Colour.Reset + " <-> Unavailable seats")
    print("")
    print("1 <-- Change the seat of ticket")
    print("2 <-- Delete ticket")
    print("3 <-- Go back")
    print("")
    return 3



def print_422(ticket) -> str:
    bigrow = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    smallrow = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    code = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T" ,"Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
    print(Colour.Red + "\u26a0\u26a0\u26a0All data of { " + ticket + " } will be delete and impossible to be recovery!\u26a0\u26a0\u26a0" + Colour.Reset)
    num_check = 0
    small_check = 0
    big_check = 0
    while num_check == 0 or small_check == 0 or big_check == 0:
        num_check = 0
        small_check = 0
        big_check = 0
        shuffle(code)
        for i in range(10):
            for j in range(26):
                if code [i] == bigrow [j]:
                    big_check = 1
                elif code [i] == smallrow [j]:
                    small_check = 1
            if code [i].isdecimal():
                num_check = 1
    temp = ""
    for i in range(10):
        temp = temp + code [i]
    print("Enter the security code to delete { " + ticket + " }.")
    print("")
    print("Security code: " + temp)
    return temp



def print_423(showing) -> str:
    bigrow = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    smallrow = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    code = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T" ,"Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
    print(Colour.Red + "\u26a0\u26a0\u26a0All data of { " + showing + " } will be delete and impossible to be recovery!\u26a0\u26a0\u26a0" + Colour.Reset)
    num_check = 0
    small_check = 0
    big_check = 0
    while num_check == 0 or small_check == 0 or big_check == 0:
        num_check = 0
        small_check = 0
        big_check = 0
        shuffle(code)
        for i in range(10):
            for j in range(26):
                if code [i] == bigrow [j]:
                    big_check = 1
                elif code [i] == smallrow [j]:
                    small_check = 1
            if code [i].isdecimal():
                num_check = 1
    temp = ""
    for i in range(10):
        temp = temp + code [i]
    print("Enter the security code to delete { " + showing + " }.")
    print("")
    print("Security code: " + temp)
    return temp



def print_424(mode, filmname, dimension, language, house) -> int or str:
    try:
        file_path = path.join(commond_path, 'Showing', 'Showing.txt')
        f = open(file_path, "r")
        while True:
            temp = f.readline()
            if temp == "":
                break
            else:
                int_showing = int(temp [1:-1]) + 1
        f.close()
        file_path = path.join(commond_path, 'Showing', 'Missshowing.txt')
        f = open(file_path, "r")
        int_miss_showing = []
        while True:
            temp = f.readline()
            if temp == "":
                break
            else:
                int_miss_showing.append(int(temp [1:-1]) + 1)
        f.close()
        for i in int_miss_showing:
            if int_showing < i:
                int_showing = i
        showing = ""
        str_showing = "S{:>{}}".format(str(int_showing), 10)
        for i in range(11):
            if str_showing [i] == " ":
                showing += "0"
            else:
                showing += str_showing [i]
    except UnboundLocalError:
        showing = "S0000000001"
    print(Colour.Underline + showing + Colour.Reset)
    print("")
    if mode == 0:
        file_path = path.join(commond_path, 'Film', 'filmname.txt')
        f = open(file_path, "r")
        count_film = int(f.readline() [:-1])
        film_list = []
        for i in range(count_film):
            film_list.append(f.readline() [:-1])
        f.close()
        len_count_film = len(str(count_film + 1))
        if count_film >= 1:
            for i in range(count_film):
                print("{:<{}} <-- Set film as {}".format(i + 1, len_count_film, film_list [i]))
            print("{:<{}} <-- Go back".format(i + 2, len_count_film, film_list))
            return i + 2
        else:
            print("There is no film")
            print("1 <-- Go back")
            return 1
    elif mode == 1:
        file_path = path.join(commond_path, 'Film', filmname, 'timelength.txt')
        f = open(file_path, "r")
        timelength = f.readline()
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'rating.txt')
        f = open(file_path, "r")
        rating = f.readline()
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
        f = open(file_path, "r")
        count_dimension = int(f.readline() [:-1])
        list_dimension = []
        for i in range(count_dimension):
            list_dimension.append(f.readline() [:-1])
        f.close()
        print("Film       : " + filmname)
        print("Time length: " + timelength + " minutes")
        print("Rating     : " + rating)
        print("")
        len_count_dimension = len(str(count_dimension + 1))
        for i in range(count_dimension):
            print("{:<{}} <-- Set dimension as {}".format(i + 1, len_count_dimension, list_dimension [i]))
        print("{:<{}} <-- Go back".format(i + 2, len_count_dimension, list_dimension))
        return i + 2
    elif mode == 2:
        file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
        f = open(file_path, "r")
        count_dimension = int(f.readline())
        temp = 0
        count_price = 0
        for i in range(count_dimension):
            temp += 1
            if count_dimension == dimension:
                count_price = temp
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'price.txt')
        f = open(file_path, "r")
        for i in range(count_price):
            f.readline()
        price = f.readline() [:-1]
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'st_price.txt')
        f = open(file_path, "r")
        for i in range(count_price):
            f.readline()
        st_price = f.readline() [:-1]
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'timelength.txt')
        f = open(file_path, "r")
        timelength = f.readline()
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'rating.txt')
        f = open(file_path, "r")
        rating = f.readline()
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
        f = open(file_path, "r")
        count_language = int(f.readline() [:-1])
        list_language = []
        for i in range(count_language):
            list_language.append(f.readline() [:-1])
        f.close()
        print("Film         : " + filmname)
        print("Dimension    : " + dimension)
        print("Price        : $" + price)
        print("Student price: $" + st_price)
        print("Time length  : " + timelength + " minutes")
        print("Rating       : " + rating)
        print("")
        len_count_language = len(str(count_language + 1))
        for i in range(count_language):
            print("{:<{}} <-- Set language as {}".format(i + 1, len_count_language, list_language [i]))
        print("{:<{}} <-- Go back".format(i + 2, len_count_language, list_language))
        return i + 2
    elif mode == 3:
        file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
        f = open(file_path, "r")
        count_dimension = int(f.readline())
        temp = 0
        count_price = 0
        for i in range(count_dimension):
            temp += 1
            if count_dimension == dimension:
                count_price = temp
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'price.txt')
        f = open(file_path, "r")
        for i in range(count_price):
            f.readline()
        price = f.readline() [:-1]
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'st_price.txt')
        f = open(file_path, "r")
        for i in range(count_price):
            f.readline()
        st_price = f.readline() [:-1]
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'timelength.txt')
        f = open(file_path, "r")
        timelength = f.readline()
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'rating.txt')
        f = open(file_path, "r")
        rating = f.readline()
        f.close()
        file_path = path.join(commond_path, 'House', 'housename.txt')
        f = open(file_path, "r")
        count_house = int(f.readline() [:-1])
        list_house = []
        for i in range(count_house):
            list_house.append(f.readline() [:-1])
        f.close()
        print("Film         : " + filmname)
        print("Dimension    : " + dimension)
        print("Language     : " + language)
        print("Price        : $" + price)
        print("Student price: $" + st_price)
        print("Time length  : " + timelength + " minutes")
        print("Rating       : " + rating)
        print("")
        len_count_house = len(str(count_house + 1))
        for i in range(count_house):
            print("{:<{}} <-- Set house as {}".format(i + 1, len_count_house, list_house [i]))
        print("{:<{}} <-- Go back".format(i + 2, len_count_house, list_house))
        return i + 2
    else:
        file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
        f = open(file_path, "r")
        count_dimension = int(f.readline())
        temp = 0
        count_price = 0
        for i in range(count_dimension):
            temp += 1
            if count_dimension == dimension:
                count_price = temp
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'price.txt')
        f = open(file_path, "r")
        for i in range(count_price):
            f.readline()
        price = f.readline() [:-1]
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'st_price.txt')
        f = open(file_path, "r")
        for i in range(count_price):
            f.readline()
        st_price = f.readline() [:-1]
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'timelength.txt')
        f = open(file_path, "r")
        timelength = f.readline()
        f.close()
        file_path = path.join(commond_path, 'Film', filmname, 'rating.txt')
        f = open(file_path, "r")
        rating = f.readline()
        f.close()
        print("Film         : " + filmname)
        print("Dimension    : " + dimension)
        print("Language     : " + language)
        print("Price        : $" + price)
        print("Student price: $" + st_price)
        print("Time length  : " + timelength + " minutes")
        print("Rating       : " + rating)
        print("House        : " + house)
        print("")
        print("Time format: DD/MM/YY HH:MM:SS")
        print("Input \"exit\" to exit")
        print("")
        return showing
    


def print_501() -> str:
    bigrow = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    smallrow = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    code = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m", "Q", "W", "E", "R", "T" ,"Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
    print(Colour.Underline + "Reset system" + Colour.Reset)
    print(Colour.Red + "\u26a0\u26a0\u26a0All data of the system will be delete and impossible to be recovery!\u26a0\u26a0\u26a0" + Colour.Reset)
    num_check = 0
    small_check = 0
    big_check = 0
    while num_check == 0 or small_check == 0 or big_check == 0:
        num_check = 0
        small_check = 0
        big_check = 0
        shuffle(code)
        for i in range(10):
            for j in range(26):
                if code [i] == bigrow [j]:
                    big_check = 1
                elif code [i] == smallrow [j]:
                    small_check = 1
            if code [i].isdecimal():
                num_check = 1
    temp = ""
    for i in range(10):
        temp = temp + code [i]
    print("Enter the security code to reset system.")
    print("")
    print("Security code: " + temp)
    return temp








































def admin_version() -> bool:
    stage = 1
    while stage != 0:
        clearscreen()
        if stage == 1:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_1()
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == 1:
                stage = 101
            elif int_input == 2:
                stage = 201
            elif int_input == 3:
                stage = 301
            elif int_input == 4:
                stage = 401
            elif int_input == 5:
                stage = 501
            elif int_input == 6:
                return 1
            else:
                clearscreen()
                list_logout = ["\\", "|", "/", "-"]
                for i in range(0, 3):
                    for j in list_logout:
                        print("\rLoging out in {} seconds {}".format(3 - i, j), end = "")
                        sleep(0.25)
                clearscreen()
                return 0
        #account
        elif stage == 101:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_101()
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == 1:
                stage = 102
            elif int_input == 2:
                stage = 105
            else:
                stage = 1
        #account > user 
        elif stage == 102:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_102()
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == 1:
                stage = 103
            elif int_input == 2:
                stage = 104
            elif int_input == 3:
                stage = 108
            else:
                stage = 101
        #account > user > change username
        elif stage == 103:
            int_input = 0
            while int_input == 0:
                print_103()
                str_input = input("")
                print(Colour.Reset)
                file_path = path.join('{}'.format(commond_path), 'Account', 'admin.txt')
                f = open(file_path, "r")
                admin_name = f.readline() [10:-1]
                if str_input == "":
                    print(Colour.Red + "YOUR INPUT CANNOT BE EMPTY" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif str_input == admin_name:
                    print(Colour.Red + "USER'S USERNAME CANNOT BE THE SAME AS AMDIN'S" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                else:
                    file_path = path.join('{}'.format(commond_path), 'Account', 'user.txt')
                    f = open(file_path, "r")
                    f.readline()
                    line = f.readline()
                    f.close()
                    line = "Username: " + str_input + "\n" + line
                    f = open(file_path, "w")
                    f.write(line)
                    f.close()
                    int_input = 1
                clearscreen()
            stage = 102
        #account > user > change password
        elif stage == 104:
            int_input = 0
            while int_input == 0:
                print_104()
                str_input = pyssword("")
                print(Colour.Reset)
                if str_input == "":
                    print(Colour.Red + "YOUR INPUT CANNOT BE EMPTY" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                else:
                    file_path = path.join('{}'.format(commond_path), 'Account', 'user.txt')
                    f = open(file_path, "r")
                    line = f.readline()
                    f.close()
                    line = line + "Password: " + str_input + "\n"
                    f = open(file_path, "w")
                    f.write(line)
                    f.close()
                    int_input = 1
                clearscreen()
            stage = 102
        #account > admin
        elif stage == 105:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_105()
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == 1:
                stage = 106
            elif int_input == 2:
                stage = 107
            elif int_input == 3:
                stage = 109
            else:
                stage = 101
        #account > admin > username
        elif stage == 106:
            int_input = 0
            while int_input == 0:
                print_106()
                str_input = input("")
                print(Colour.Reset)
                file_path = path.join('{}'.format(commond_path), 'Account', 'user.txt')
                f = open(file_path, "r")
                user_name = f.readline() [10:-1]
                if str_input == "":
                    print(Colour.Red + "YOUR INPUT CANNOT BE EMPTY" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif str_input == user_name:
                    print(Colour.Red + "ADMIN'S USERNAME CANNOT BE THE SAME AS USER'S" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                else:
                    file_path = path.join('{}'.format(commond_path), 'Account', 'admin.txt')
                    f = open(file_path, "r")
                    f.readline()
                    line = f.readline()
                    f.close()
                    line = "Username: " + str_input + "\n" + line
                    f = open(file_path, "w")
                    f.write(line)
                    f.close()
                    int_input = 1
                clearscreen()
            stage = 105
        #account > admin > password
        elif stage == 107:
            int_input = 0
            while int_input == 0:
                print_107()
                str_input = pyssword("")
                print(Colour.Reset)
                if str_input == "":
                    print(Colour.Red + "YOUR INPUT CANNOT BE EMPTY" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                else:
                    file_path = path.join('{}'.format(commond_path), 'Account', 'admin.txt')
                    f = open(file_path, "r")
                    line = f.readline()
                    f.close()
                    line = line + "Password: " + str_input + "\n"
                    f = open(file_path, "w")
                    f.write(line)
                    f.close()
                    int_input = 1
                clearscreen()
            stage = 105
        #account > user > login time
        elif stage == 108:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_108()
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            stage = 102
        #account > admin > login time
        elif stage == 109:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_109()
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            stage = 105
        #house
        elif stage == 201:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_201()
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            file_path = path.join('{}'.format(commond_path), 'House', 'housename.txt')
            f = open(file_path, "r")
            for i in range(int_input):
                f.readline()
            house: str = f.readline() [:-1]
            f.close()
            if int_input == choose:
                stage = 1
            elif int_input == choose - 1:
                stage = 207
            else:
                stage = 202
        #house > seatingplan
        elif stage == 202:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_202(house)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == 1:
                stage = 203
            elif int_input == 2:
                stage = 205
            elif int_input == 3:
                stage = 206
            else:
                stage = 201
        #house > seatingplan > row and column
        elif stage == 203:
            file_path = path.join('{}'.format(commond_path), 'House', '{}'.format(house), 'houseplan.txt')
            f = open(file_path)
            seating_plan = []
            row = 0
            while True:
                line = f.readline()
                if line == "":
                    break
                row += 1
                temp = []
                i = 0
                while True:
                    if line [i] == "\n":
                        break
                    else:
                        column = len(line [:-1])
                        temp.append(line [i])
                        i += 1
                seating_plan.append(temp)
            f.close()
            int_input = -1
            while int_input == -1:
                row_input = -1
                while row_input == -1:
                    clearscreen()
                    print_203(house)
                    row_strinput = input("Which row for changing status: ")
                    if row_strinput == "exit" or row_strinput == "Exit" or row_strinput == "EXIT":
                        row_input = row
                        int_input = 0
                    else:
                        row_input = eng_to_int(row_strinput)
                        if row_input == -1:
                            print(Colour.Red + "YOUR INPUT IS INCORRECT" + Colour.Reset)
                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                        elif row_input < row:
                            column_strinput = input("Which column for changing status: ")
                            if column_strinput == "exit" or column_strinput == "Exit" or column_strinput == "EXIT":
                                row_input = row
                                int_input = 0
                            else:
                                if column_strinput.isdecimal() and int(column_strinput) != 0 and int(column_strinput) <= column:
                                    column_input = int(column_strinput) - 1
                                    int_input = 1
                                else:
                                    print(Colour.Red + "YOUR INPUT IS INCORRECT" + Colour.Reset)
                                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                        else:
                            print(Colour.Red + "YOUR INPUT IS INCORRECT" + Colour.Reset)
                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
            if int_input == 0:
                stage = 202
            else:
                stage = 204
        #house > seatingplan > row and column > change status
        elif stage == 204:
            int_input = 0
            while int_input == 0 or int_input > 2:
                seat = print_204(house, row_input, column_input)
                int_input = input_int_check("Input number: ", 2)
                clearscreen()
            if int_input == 2:
                stage = 203
            else:
                file_path = path.join('{}'.format(commond_path), 'House', '{}'.format(house), 'houseplan.txt')
                line = []
                f = open(file_path, "r")
                for j in range(row):
                    line.append(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write("")
                f.close()
                f = open(file_path, "a")
                for j in range(row):
                    if j == row_input:
                        for k in range(column + 1):
                            if k == column_input:
                                if seat == 0:
                                    f.write("2")
                                else:
                                    f.write("0")
                            else:
                                f.write(line [j][k])
                    else:
                        f.write(line [j])
                f.close()
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'showingnum.txt')
                f = open(file_path, "r")
                count_showing = int(f.readline())
                f.close()
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'showing.txt')
                f = open(file_path, "r")
                for i in range(count_showing):
                    f.readline()
                    temp = f.readline() [:-1]
                    g = open(path.join(commond_path, 'Showing', temp, 'houseplan.txt'), "r")
                    line = ""
                    for j in range(row):
                        if j == row_input:
                            temp1 = g.readline()
                            for k in range(column + 1):
                                if k == column_input:
                                    if seat != 2:
                                        line += "2"
                                    else:
                                        line += "0"
                                else:
                                    line += temp1 [k]
                        else:
                            line += g.readline()
                    g = open(path.join(commond_path, 'Showing', temp, 'houseplan.txt'), 'w')
                    g.write(line)
                    g.close()
                f.close()
                stage = 203
        #house > seatingplan > rename
        elif stage == 205:
            int_input = 0
            print_205(house)
            str_input = input("")
            while str_input != "" and str_input [0] == " ":
                temp = ""
                for i in range(1, len(str_input)):
                    temp += str_input [i]
                str_input = temp
            while str_input != "" and (str_input [len(str_input) - 1] == " " or str_input [len(str_input) - 1] == "."):
                temp = ""
                for i in range(0, len(str_input) - 1):
                    temp += str_input [i]
                str_input = temp
            if str_input == "":
                print(Colour.Red + "NAME OF A HOUSE CANNOT BE EMPTY" + Colour.Reset)
                input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
            elif file_name_include(str_input) == False:
                str_input = ""
                print(Colour.Red + "NAME OF A HOUSE CANNOT INCLUDE \/:*?\"<>|" + Colour.Reset)
                input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
            elif file_name_include_ascii(str_input) == False:
                str_input = ""
                print(Colour.Red + "NAME OF A HOUSE MUST BE WITHIN ASCII 32 to 126" + Colour.Reset)
                input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
            file_path = path.join(commond_path, "House", "housename.txt")
            f = open(file_path, "r")
            count_house = int(f.readline() [:-1])
            for i in range(count_house):
                if str_input.upper() == f.readline().upper() and str_input.upper() != house.upper():
                    str_input = ""
                    print(Colour.Red + "NAME OF A HOUSE CANNOT BE THE SAME AS OTHER HOUSES" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
            else:
                file_path = path.join(commond_path, 'House', 'housename.txt')
                line = []
                f = open(file_path, "r")
                count_house = int(f.readline() [:-1])
                for i in range(count_house):
                    line.append(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write("")
                f.close()
                f = open(file_path, "a")
                str_count_house = str(count_house) + "\n"
                f.write(str_count_house)
                for i in range(count_house):
                    if line [i] == house + "\n":
                        f.write("House " + str_input + "\n")
                    else:
                        f.write(line [i])
                f.close()
                file_path = path.join(commond_path, 'House', house)
                rename(file_path, path.join(commond_path, 'House', 'House {}'.format(str_input)))
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showingnum.txt')
                f = open(file_path, "r")
                count_showing = int(f.readline())
                f.close()
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showing.txt')
                f = open(file_path, "r")
                list_showing = []
                for i in range(count_showing):
                    f.readline()
                    list_showing.append(f.readline() [:-1])
                f.close()
                for i in list_showing:
                    file_path = path.join(commond_path, 'Showing', i, 'house.txt')
                    f = open(file_path, "w")
                    f.write("House " + str_input)
                    f.close()
                rename(path.join(commond_path, 'Showing', '__House information', house), path.join(commond_path, 'Showing', '__House information', "House " + str_input))
                house = "House " + str_input
                housename_accord()
                stage = 201
        #house > seatingplan > delete
        elif stage == 206:
            int_input = 0
            verification_code = print_206(house)
            record = input("")
            if record == verification_code:
                int_input = 1
                file_path = path.join(commond_path, 'House', 'housename.txt')
                line = []
                f = open(file_path, "r")
                count_house = int(f.readline() [:-1])
                for i in range(count_house):
                    line.append(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write("")
                f.close()
                f = open(file_path, "a")
                f.write(str(count_house - 1) + "\n")
                for i in range(count_house):
                    if line [i] != house + "\n":
                        f.write(line [i])
                f.close()
                file_path = path.join(commond_path, 'House', house, 'allseat.txt')
                remove(file_path)
                file_path = path.join(commond_path, 'House', house, 'houseplan.txt')
                remove(file_path)
                rmdir(path.join(commond_path, 'House', house))
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showingnum.txt')
                f = open(file_path, "r")
                count_showing = int(f.readline())
                f.close()
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showing.txt')
                f = open(file_path, "r")
                for i in range(count_showing):
                    f.readline()
                    temp = f.readline() [:-1]
                    g = open(path.join(commond_path, 'Showing', temp, 'film.txt'), "r")
                    filmname = g.readline() [:-1]
                    dimension = g.readline() [:-1]
                    language = g.readline() [:-1]
                    g.close()
                    g = open(path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showingnum.txt'), "r")
                    count_showing_film = int(g.readline())
                    g.close()
                    g = open(path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showing.txt'), "r")
                    line = ""
                    for i in range(count_showing_film):
                        temp1 = g.readline()
                        temp2 = g.readline()
                        if temp2 [:-1] != temp:
                            line += temp1 + temp2
                    g.close()
                    g = open(path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showingnum.txt'), "w")
                    g.write(str(count_showing_film - 1))
                    g.close()
                    g = open(path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showing.txt'), "w")
                    g.write(line)
                    g.close()
                    g = open(path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt'), "r")
                    count_showing_time = int(g.readline())
                    g.close()
                    g = open(path.join(commond_path, 'Showing', '__Time information', 'Showing.txt'), "r")
                    line = ""
                    for i in range(count_showing_time):
                        temp1 = g.readline()
                        temp2 = g.readline()
                        if temp2 [:-1] != temp:
                            line += temp1 + temp2
                    g.close()
                    g = open(path.join(commond_path, 'Showing', '__Time information', 'Time.txt'), "r")
                    line1 = ""
                    for i in range(count_showing_time):
                        temp1 = g.readline()
                        temp2 = g.readline()
                        temp3 = g.readline()
                        if temp3 [:-1] != temp:
                            line1 += temp1 + temp2 + temp3
                    g.close()
                    g = open(path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt'), "w")
                    g.write(str(count_showing_time - 1))
                    g.close()
                    g = open(path.join(commond_path, 'Showing', '__Time information', 'Showing.txt'), "w")
                    g.write(line)
                    g.close()
                    g = open(path.join(commond_path, 'Showing', '__Time information', 'time.txt'), "w")
                    g.write(line1)
                    g.close()
                    g = open(path.join(commond_path, 'Showing', 'Showingnum.txt'), "r")
                    count_showing_time = int(g.readline())
                    g.close()
                    g = open(path.join(commond_path, 'Showing', 'Showing.txt'), "r")
                    line = ""
                    for i in range(count_showing_time):
                        temp1 = g.readline()
                        temp2 = g.readline()
                        if temp2 [:-1] != temp:
                            line += temp1 + temp2
                    g.close()
                    g = open(path.join(commond_path, 'Showing', 'Showingnum.txt'), "w")
                    g.write(str(count_showing_time - 1))
                    g.close()
                    g = open(path.join(commond_path, 'Showing', 'Showing.txt'), "w")
                    g.write(line)
                    g.close()
                    g = open(path.join(commond_path, 'Showing', 'Missshowing.txt'), "a")
                    g.write(temp + "\n")
                    g.close()
                    remove(path.join(commond_path, 'Showing', temp, 'film.txt'))
                    remove(path.join(commond_path, 'Showing', temp, 'house.txt'))
                    remove(path.join(commond_path, 'Showing', temp, 'houseplan.txt'))
                    remove(path.join(commond_path, 'Showing', temp, 'ticket.txt'))
                    remove(path.join(commond_path, 'Showing', temp, 'starttime.txt'))
                    rmdir(path.join(commond_path, 'Showing', temp))
                f.close()
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showing.txt')
                remove(file_path)
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showingnum.txt')
                remove(file_path)
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Time.txt')
                remove(file_path)
                rmdir(path.join(commond_path, 'Showing', '__House information', house))
            if int_input == 0:
                stage = 202
            else:
                stage = 201
        #house > creation
        elif stage == 207:
            name = ""
            while name == "":
                clearscreen()
                name = input("What is the name of the new house: ")
                while name != "" and name [0] == " ":
                    temp = ""
                    for i in range(1, len(name)):
                        temp += name [i]
                    name = temp
                while name != "" and (name [len(name) - 1] == " " or name [len(name) - 1] == "."):
                    temp = ""
                    for i in range(0, len(name) - 1):
                        temp += name [i]
                    name = temp
                if name == "":
                    print(Colour.Red + "NAME OF A HOUSE CANNOT BE EMPTY" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif file_name_include(name) == False:
                    name = ""
                    print(Colour.Red + "NAME OF A HOUSE CANNOT INCLUDE \/:*?\"<>|" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif file_name_include_ascii(name) == False:
                    name = ""
                    print(Colour.Red + "NAME OF A HOUSE MUST BE WITHIN ASCII 32 to 126" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                file_path = path.join(commond_path, "House", "housename.txt")
                f = open(file_path, "r")
                count_house = int(f.readline() [:-1])
                for i in range(count_house):
                    if name.upper() == f.readline().upper() and name.upper() != house.upper():
                        name = ""
                        print(Colour.Red + "NAME OF A HOUSE CANNOT BE THE SAME AS OTHER HOUSES" + Colour.Reset)
                        input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
            print("")
            row = 0
            while row == 0:
                row = input("What is the row of House {}: ".format(name))
                if row.isdecimal() and int(row) != 0:
                    row = int(row)
                else:
                    row = 0
                    print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                    clearscreen()
                    print("What is the name of the new house: " + name)
                    print("")
            column = 0
            while column == 0:
                column = input("What is the column of House {}: ".format(name))
                if column.isdecimal() and int(column) != 0:
                    column = int(column)
                else:
                    column = 0
                    print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                    clearscreen()
                    print("What is the name of the new house: " + name)
                    print("")
                    print("What is the row of House {}: ".format(name) + str(row))
            if not path.exists(path.join(commond_path, 'House', 'House {}'.format(name))):
                mkdir(path.join(commond_path, 'House', 'House {}'.format(name)))
            file_path = path.join(commond_path, 'House', 'housename.txt')
            line = []
            f = open(file_path, "r")
            count_house = int(f.readline() [:-1]) + 1
            for i in range(count_house - 1):
                line.append(f.readline())
            f.close()
            f = open(file_path, "w")
            f.write("")
            f.close()
            f = open(file_path, "a")
            f.write(str(count_house) + "\n")
            for i in range(count_house - 1):
                f.write(line [i])
            f.write("House {}\n".format(name))
            f.close()
            file_path = path.join(commond_path, 'House', 'House {}'.format(name), 'allseat.txt')
            f = open(file_path, "w")
            f.write(str(row * column))
            f.close()
            file_path = path.join(commond_path, 'House', 'House {}'.format(name), 'houseplan.txt')
            f = open(file_path, "w")
            f.write("")
            f.close()
            f = open(file_path, "a")
            for i in range(row):
                for j in range(column):
                    f.write("0")
                f.write("\n")
            f.close()
            house = "House " + name
            if not path.exists(path.join(commond_path, 'Showing', '__House information', house)):
                mkdir(path.join(commond_path, 'Showing', '__House information', house))
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showing.txt')
                f = open(file_path, "w")
                f.write("")
                f.close()
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showingnum.txt')
                f = open(file_path, "w")
                f.write("0")
                f.close()
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Time.txt')
                f = open(file_path, "w")
                f.write("")
                f.close()
            housename_accord()
            stage = 202
        #film
        elif stage == 301:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_301()
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 1
            elif int_input == choose - 1:
                stage = 314
            else:
                file_path = path.join(commond_path, 'Film', 'filmname.txt')
                f = open(file_path, "r")
                for i in range(int_input):
                    f.readline()
                filmname = f.readline() [:-1]
                stage = 302
        #film > data
        elif stage == 302:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_302(filmname)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == 1:
                stage = 303
            elif int_input == 2:
                stage = 304
            elif int_input == 3:
                stage = 305
            elif int_input == 4:
                stage = 306
            elif int_input == 5:
                stage = 309
            elif int_input == 6:
                stage = 312
            elif int_input == 7:
                stage = 313
            else:
                stage = 301
        #film > data > name
        elif stage == 303:
            file_path = path.join(commond_path, 'Film', 'filmname.txt')
            f = open(file_path, "r")
            count_film = int(f.readline() [:-1])
            line = []
            for i in range(count_film):
                line.append(f.readline() [:-1])
            f.close()
            str_input = ""
            while str_input == "":
                clearscreen()
                print(Colour.Underline + "{}".format(filmname) + Colour.Reset)
                print("")
                print("Current name: " + filmname)
                str_input = input("The new name: ")
                while str_input != "" and str_input [0] == " ":
                    temp = ""
                    for i in range(1, len(str_input)):
                        temp += str_input [i]
                    str_input = temp
                while str_input != "" and (str_input [len(str_input) - 1] == " " or str_input [len(str_input) - 1] == "."):
                    temp = ""
                    for i in range(0, len(str_input) - 1):
                        temp += str_input [i]
                    str_input = temp
                if str_input == "":
                    print(Colour.Red + "FILM NAME CANNOT BE EMPTY" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif str_input.upper() == "Film addition".upper():
                    str_input = ""
                    print(Colour.Red + "FILM NAME CANNOT BE \"Film addition\"" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif str_input.upper() == "Go back".upper():
                    str_input = ""
                    print(Colour.Red + "FILM NAME CANNOT BE \"Go back\"" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif file_name_include(str_input) == False:
                    str_input = ""
                    print(Colour.Red + "FILM NAME CANNOT INCLUDE \/:*?\"<>|" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif file_name_include_ascii(str_input) == False:
                    str_input = ""
                    print(Colour.Red + "FILM NAME MUST BE WITHIN ASCII 32 to 126" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                for i in range(count_film):
                    if str_input.upper() == line [i].upper() and str_input != filmname:
                        str_input = ""
                        print(Colour.Red + "FILM NAME CANNOT BE THE SAME AS OTHER FILMS" + Colour.Reset)
                        input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
            file_path = path.join(commond_path, 'Film', 'filmname.txt')
            line = []
            f = open(file_path, "r")
            count_film = int(f.readline() [:-1])
            for i in range(count_film):
                line.append(f.readline())
            f.close()
            f = open(file_path, "w")
            f.write("")
            f.close()
            f = open(file_path, "a")
            str_count_film = str(count_film) + "\n"
            f.write(str_count_film)
            for i in range(count_film):
                if line [i] == filmname + "\n":
                    f.write(str_input + "\n")
                else:
                    f.write(line [i])
            f.close()
            file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
            f = open(file_path, "r")
            count_showing = int(f.readline())
            f.close()
            file_path = path.join(commond_path, 'Showing', 'Showing.txt')
            f = open(file_path, "r")
            list_showing = []
            for i in range(count_showing):
                list_showing.append(f.readline() [:-1])
            f.close()
            for i in list_showing:
                file_path = path.join(commond_path, 'Showing', i, 'film.txt')
                f = open(file_path, "r")
                f.readline()
                line = f.readline()
                line += f.readline()
                f.close()
                f = open(file_path, "w")
                f.write(str_input + "\n" + line)
                f.close()
            rename(path.join(commond_path, 'Showing', '__Film information', filmname), path.join(commond_path, 'Showing', '__Film information', str_input))
            rename(path.join(commond_path, 'Film', filmname), path.join(commond_path, 'Film', str_input))
            filmname_accord()
            filmname = str_input
            stage = 302
        #film > data > timelength
        elif stage == 304:
            file_path = path.join(commond_path, 'Film', filmname, 'timelength.txt')
            f = open(file_path, "r")
            timelength = f.readline()
            f.close()
            print(Colour.Underline + filmname + Colour.Reset)
            print("")
            print("Current time length (minutes): " + timelength)
            str_input = input("The new time length (minutes): ")
            while str_input != "" and str_input [0] == " ":
                temp = ""
                for i in range(1, len(str_input)):
                    temp += str_input [i]
                str_input = temp
            while str_input != "" and str_input [len(str_input) - 1] == " ":
                temp = ""
                for i in range(0, len(str_input) - 1):
                    temp += str_input [i]
                str_input = temp
            if str_input.isdecimal() and int(str_input) != 0:
                error = 0
                file_path = path.join(commond_path, 'House', 'housename.txt')
                f = open(file_path, "r")
                count_house = int(f.readline() [:-1])
                house_list = []
                for i in range(count_house):
                    house_list.append(f.readline() [:-1])
                for house in house_list:
                    format_time = "%d/%m/%y %H:%M:%S"
                    file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showingnum.txt')
                    f = open(file_path, "r")
                    count_showing_time = int(f.readline())
                    f.close()
                    file_path = path.join(commond_path, 'Showing', '__House information', house, 'Time.txt')
                    f = open(file_path, "r")
                    start_time = []
                    end_time = []
                    showing_time = []
                    timelength_time = []
                    for i in range(count_showing_time):
                        line1 = f.readline() [:-1]
                        line2 = int(f.readline() [:-1])
                        line3 = f.readline() [:-1]
                        g = open(path.join(commond_path, 'Showing', line3, 'film.txt'))
                        if g.readline() [:-1] == filmname:
                            start_time.append(datetime.strptime(line1, format_time))
                            timelength_time.append(str_input)
                            end_time.append(datetime.strptime(line1, format_time) + timedelta(minutes = int(str_input)))
                            showing_time.append(line3)
                        else:
                            start_time.append(datetime.strptime(line1, format_time))
                            timelength_time.append(str(line2))
                            end_time.append(datetime.strptime(line1, format_time) + timedelta(minutes = line2))
                            showing_time.append(line3)
                        g.close()
                    f.close()
                    for i in range(count_showing_time - 1):
                        for j in range(count_showing_time - 1 - i):
                            if start_time [j] > start_time [j + 1]:
                                temp = start_time [j]
                                start_time [j] = start_time [j + 1]
                                start_time [j + 1] = temp
                                temp = end_time [j]
                                end_time [j] = end_time [j + 1]
                                end_time [j + 1] = temp
                                temp = showing_time [j]
                                showing_time [j] = showing_time [j + 1]
                                showing_time [j + 1] = temp
                                temp = timelength_time [j]
                                timelength_time [j] = timelength_time [j + 1]
                                timelength_time [j + 1] = temp
                    for i in range(count_showing_time - 1):
                        if start_time [i] <= start_time [i + 1] and end_time [i] > start_time [i + 1] and error == 0:
                            error = 1
                        elif start_time [i + 1] <= start_time [i] and end_time [i + 1] > start_time [i] and error == 0:
                            error = 1
                if error == 0:
                    file_path = path.join(commond_path, 'House', 'housename.txt')
                    f = open(file_path, "r")
                    f.readline() [:-1]
                    house_list = []
                    for i in range(count_house):
                        house_list.append(f.readline() [:-1])
                    f.close()
                    file_path = path.join(commond_path, 'Showing', 'Showing.txt')
                    f = open(file_path, "r")
                    showing_list = []
                    while True:
                        temp = f.readline()
                        if temp == "":
                            break
                        else:
                            showing_list.append(temp [:-1])
                    f.close()
                    for i in showing_list:
                        file_path = path.join(commond_path, 'Showing', '__Time information', 'Time.txt')
                        f = open(file_path, "r")
                        line = ""
                        while True:
                            temp1 = f.readline()
                            temp2 = f.readline()
                            temp3 = f.readline()
                            if temp1 == "":
                                break
                            elif temp3 [:-1] == i:
                                line += temp1 + str_input + "\n" + temp3
                            else:
                                line += temp1 + temp2 + temp3
                        f.close()
                        f = open(file_path, "w")
                        f.write(line)
                        f.close()
                        for j in house_list:
                            file_path = path.join(commond_path, 'Showing', '__House information', j, 'Time.txt')
                            f = open(file_path, "r")
                            line = ""
                            while True:
                                temp1 = f.readline()
                                temp2 = f.readline()
                                temp3 = f.readline()
                                if temp1 == "":
                                    break
                                elif temp3 [:-1] == i:
                                    line += temp1 + str_input + "\n" + temp3
                                else:
                                    line += temp1 + temp2 + temp3
                            f.close()
                            f = open(file_path, "w")
                            f.write(line)
                            f.close()
                    file_path = path.join(commond_path, 'Film', filmname, 'timelength.txt')
                    f = open(file_path, "w")
                    f.write(str_input)
                    f.close()
                    stage = 302
                else:
                    print(Colour.Red + "THERE WILL BE OVERLAPPING SHOWINGS" + Colour.Reset)
                    input(Colour.Yellow + "PRESS ENTER TO RETRY" + Colour.Reset)
            else:
                print(Colour.Red + "YOUR INPUT IS INCORRECT" + Colour.Reset)
                input(Colour.Yellow + "PRESS ENTER TO RETRY" + Colour.Reset)
        #film > data > rating
        elif stage == 305:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_305(filmname)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 302
            else:
                rating = ["I", "IIA", "IIB", "III"]
                file_path = path.join(commond_path, 'Film', filmname, 'rating.txt')
                f = open(file_path, "r")
                c_rating = f.readline()
                f.close()
                for i in range(3):
                    if rating [i] == c_rating:
                        temp = rating [i]
                        rating [i] = rating [i + 1]
                        rating [i + 1] = temp
                int_input -= 1
                f = open(file_path, "w")
                f.write(rating [int_input])
                f.close()
                stage = 302
        #film > data > language
        elif stage == 306:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_306(filmname)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == 1:
                stage = 307
            elif int_input == 2:
                stage = 308
            else:
                stage = 302
        #film > data > language > addition
        elif stage == 307:
            file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
            f = open(file_path, "r")
            count_language = int(f.readline() [:-1])
            line = []
            for i in range(count_language):
                line.append(f.readline() [:-1])
            f.close()
            str_input = ""
            while str_input == "":
                clearscreen()
                print_307(filmname)
                str_input = input("Additive language: ")
                while str_input != "" and str_input [0] == " ":
                    temp = ""
                    for i in range(1, len(str_input)):
                        temp += str_input [i]
                    str_input = temp
                while str_input != "" and (str_input [len(str_input) - 1] == " " or str_input [len(str_input) - 1] == "."):
                    temp = ""
                    for i in range(0, len(str_input) - 1):
                        temp += str_input [i]
                    str_input = temp
                if str_input == "":
                    print(Colour.Red + "NAME OF A LANGUAGE CANNOT BE EMPTY" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif file_name_include(str_input) == False:
                    str_input = ""
                    print(Colour.Red + "NAME OF A LANGUAGE CANNOT INCLUDE \/:*?\"<>|" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif file_name_include_ascii(str_input) == False:
                    str_input = ""
                    print(Colour.Red + "NAME OF A LANGUAGE MUST BE WITHIN ASCII 32 to 126" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                for i in range(count_language):
                    if str_input.upper() == line [i].upper():
                        str_input = 0
            if str_input == 0:
                stage = 306
            else:
                f = open(file_path, "w")
                f.write("")
                f.close()
                f = open(file_path, "a")
                str_count_language = str(count_language + 1) + "\n"
                f.write(str_count_language)
                for i in range(count_language):
                    f.write(line [i] + "\n")
                f.write(str_input + "\n")
                f.close()
                file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
                f = open(file_path, "r")
                count_dimension = int(f.readline() [:-1])
                dimension_list = []
                for i in range(count_dimension):
                    dimension_list.append(f.readline() [:-1])
                f.close()
                for i in dimension_list:
                    if not path.exists(path.join(commond_path, 'Showing', '__Film information', filmname, i, str_input)):
                        mkdir(path.join(commond_path, 'Showing', '__Film information', filmname, i, str_input))
                    file_path = path.join(commond_path, 'Showing', '__Film information', filmname, i, str_input, 'Showing.txt')
                    f = open(file_path, "w")
                    f.write("")
                    f.close()
                    file_path = path.join(commond_path, 'Showing', '__Film information', filmname, i, str_input, 'Showingnum.txt')
                    f = open(file_path, "w")
                    f.write("0")
                    f.close()
                stage = 306
        #film > data > language > deletion
        elif stage == 308:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_308(filmname)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 306
            else:
                file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
                f = open(file_path, "r")
                count_language = int(f.readline() [:-1])
                line = []
                for i in range(count_language):
                    line.append(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write("")
                f.close()
                f = open(file_path, "a")
                str_count_language = str(count_language - 1) + "\n"
                f.write(str_count_language)
                for i in range(count_language):
                    if i != int_input - 1:
                        f.write(line [i])
                    else:
                        delete_language = line [i][:-1]
                f.close()
                file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
                f = open(file_path, "r")
                count_dimension = int(f.readline() [:-1])
                list_dimension = []
                for i in range(count_dimension):
                    list_dimension.append(f.readline() [:-1])
                f.close()
                list_showing = []
                for i in list_dimension:
                    file_path = path.join(commond_path, 'Showing', '__Film information', filmname, i, delete_language, 'Showingnum.txt')
                    f = open(file_path, "r")
                    count_showing = int(f.readline())
                    f.close()
                    remove(file_path)
                    file_path = path.join(commond_path, 'Showing', '__Film information', filmname, i, delete_language, 'Showing.txt')
                    f = open(file_path, "r")
                    for j in range(count_showing):
                        f.readline()
                        list_showing.append(f.readline() [:-1])
                    f.close()
                    remove(file_path)
                    rmdir(path.join(commond_path, 'Showing', '__Film information', filmname, i, delete_language))
                file_path = path.join(commond_path, 'House', 'housename.txt')
                f = open(file_path, "r")
                count_house = int(f.readline() [:-1])
                list_house = []
                for j in range(count_house):
                    list_house.append(f.readline() [:-1])
                f.close()
                for i in list_house:
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Showingnum.txt')
                    f = open(file_path, "r")
                    count_showing = int(f.readline())
                    str_count_showing = count_showing
                    f.close()
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Showing.txt')
                    f = open(file_path, "r")
                    g = open(path.join(commond_path, 'Showing', '__House information', i, 'Time.txt'))
                    line = ""
                    line1 = ""
                    for j in range(count_showing):
                        temp1 = f.readline()
                        temp2 = f.readline()
                        temp3 = g.readline()
                        temp4 = g.readline()
                        temp5 = g.readline()
                        if not temp2 [:-1] in list_showing:
                            line += temp1 + temp2
                        else:
                            str_count_showing -= 1
                        if not temp5 [:-1] in list_showing:
                            line1 += temp3 + temp4 + temp5
                    f.close()
                    g.close()
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Showingnum.txt')
                    f = open(file_path, "w")
                    f.write(str(str_count_showing))
                    f.close()
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Showing.txt')
                    f = open(file_path, "w")
                    f.write(line)
                    f.close()
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Time.txt')
                    f = open(file_path, "w")
                    f.write(line1)
                    f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt')
                f = open(file_path, "r")
                count_showing = int(f.readline())
                str_count_showing = count_showing
                f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showing.txt')
                f = open(file_path, "r")
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Time.txt')
                g = open(file_path, "r")
                line = ""
                line1 = ""
                for j in range(count_showing):
                    temp1 = f.readline()
                    temp2 = f.readline()
                    temp3 = g.readline()
                    temp4 = g.readline()
                    temp5 = g.readline()
                    if not temp2 [:-1] in list_showing:
                        line += temp1 + temp2
                    else:
                        str_count_showing -= 1
                    if not temp5 [:-1] in list_showing:
                        line1 += temp3 + temp4 + temp5
                f.close()
                g.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt')
                f = open(file_path, "w")
                f.write(str(str_count_showing))
                f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showing.txt')
                f = open(file_path, "w")
                f.write(line)
                f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Time.txt')
                f = open(file_path, "w")
                f.write(line1)
                f.close()
                for i in list_showing:
                    remove(path.join(commond_path, 'Showing', i, 'film.txt'))
                    remove(path.join(commond_path, 'Showing', i, 'house.txt'))
                    remove(path.join(commond_path, 'Showing', i, 'houseplan.txt'))
                    remove(path.join(commond_path, 'Showing', i, 'starttime.txt'))
                    remove(path.join(commond_path, 'Showing', i, 'ticket.txt'))
                    rmdir(path.join(commond_path, 'Showing', i))
                    file_path = path.join(commond_path, 'Showing', 'Missshowing.txt')
                    f = open(file_path, "a")
                    f.write(i + "\n")
                    f.close()
                    file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
                    f = open(file_path, "r")
                    count_showing = int(f.readline())
                    f.close()
                    file_path = path.join(commond_path, 'Showing', 'Showing.txt')
                    f = open(file_path, "r")
                    line = ""
                    for j in range(count_showing):
                        temp = f.readline()
                        if not temp [:-1] in list_showing:
                            line += temp
                    f.close()
                    file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
                    f = open(file_path, "w")
                    f.write(str(count_showing - 1))
                    f.close()
                    file_path = path.join(commond_path, 'Showing', 'Showing.txt')
                    f = open(file_path, "w")
                    f.write(line)
                    f.close()
                stage = 306
        #film > data > dimension
        elif stage == 309:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_309(filmname)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == 1:
                stage = 310
            elif int_input == 2:
                stage = 311
            else:
                stage = 302
        #film > data > dimension > addition
        elif stage == 310:
            file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
            f = open(file_path, "r")
            count_dimension = int(f.readline() [:-1])
            line = []
            for i in range(count_dimension):
                line.append(f.readline() [:-1])
            f.close()
            str_input = ""
            while str_input == "":
                clearscreen()
                print_310(filmname)
                str_input = input("Additive dimension: ").upper()
                while str_input != "" and str_input [0] == " ":
                    temp = ""
                    for i in range(1, len(str_input)):
                        temp += str_input [i]
                    str_input = temp
                while str_input != "" and (str_input [len(str_input) - 1] == " " or str_input [len(str_input) - 1] == " "):
                    temp = ""
                    for i in range(0, len(str_input) - 1):
                        temp += str_input [i]
                    str_input = temp
                if str_input == "":
                    print(Colour.Red + "NAME OF A DIMENSION CANNOT BE EMPTY" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif str_input [:-1].isdigit() and (str_input [len(str_input) - 1] == "D" or str_input [len(str_input) - 1] == "d"):
                    str_input = str_input [:-1] + "D"
                else:
                    str_input = ""
                    print(Colour.Red + "NAME OF A DIMENSION MUST BE \"\{INTEGER\}\"" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                for i in range(count_dimension):
                    if str_input == line [i]:
                        str_input = 0
            if str_input == 0:
                stage = 309
            else:
                line.append(str_input)
                file_path = path.join(commond_path, 'Film', filmname, 'price.txt')
                f = open(file_path, "r")
                line_1 = []
                for i in range(count_dimension):
                    line_1.append(f.readline() [:-1])
                f.close()
                file_path = path.join(commond_path, 'Film', filmname, 'st_price.txt')
                f = open(file_path, "r")
                line_2 = []
                for i in range(count_dimension):
                    line_2.append(f.readline() [:-1])
                f.close()
                line_1.append("0")
                for i in range(count_dimension, 0, -1):
                    if int(line [i][:-1]) < int(line [i - 1][:-1]):
                        temp = line [i]
                        line [i] = line [i - 1]
                        line [i - 1] = temp
                        temp = line_1 [i]
                        line_1 [i] = line_1 [i - 1]
                        line_1 [i - 1] = temp
                        temp = line_2 [i]
                        line_2 [i] = line_2 [i - 1]
                        line_2 [i - 1] = temp
                file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
                f = open(file_path, "w")
                f.write("")
                f.close()
                f = open(file_path, "a")
                str_count_dimension = str(count_dimension + 1) + "\n"
                f.write(str_count_dimension)
                for i in range(count_dimension + 1):
                    f.write(line [i] + "\n")
                f.close()
                file_path = path.join(commond_path, 'Film', filmname, 'price.txt')
                f = open(file_path, "w")
                f.write("")
                f.close()
                f = open(file_path, "a")
                for i in range(count_dimension + 1):
                    f.write(line_1 [i] + "\n")
                f.close()
                file_path = path.join(commond_path, 'Film', filmname, 'st_price.txt')
                f = open(file_path, "w")
                f.write("")
                f.close()
                f = open(file_path, "a")
                for i in range(count_dimension + 1):
                    f.write(line_2 [i] + "\n")
                f.close()
                file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
                f = open(file_path, "r")
                count_language = int(f.readline() [:-1])
                language_list = []
                for i in range(count_language):
                    language_list.append(f.readline() [:-1])
                f.close()
                if not path.exists(path.join(commond_path, 'Showing', '__Film information', filmname, str_input)):
                    mkdir(path.join(commond_path, 'Showing', '__Film information', filmname, str_input))
                for i in language_list:
                    if not path.exists(path.join(commond_path, 'Showing', '__Film information', filmname, str_input, i)):
                        mkdir(path.join(commond_path, 'Showing', '__Film information', filmname, str_input, i))
                    file_path = path.join(commond_path, 'Showing', '__Film information', filmname, str_input, i, 'Showing.txt')
                    f = open(file_path, "w")
                    f.write("")
                    f.close()
                    file_path = path.join(commond_path, 'Showing', '__Film information', filmname, str_input, i, 'Showingnum.txt')
                    f = open(file_path, "w")
                    f.write("0")
                    f.close()
                stage = 309
        #film > data > dimension > deletion
        elif stage == 311:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_311(filmname)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 309
            else:
                file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
                f = open(file_path, "r")
                count_dimension = int(f.readline() [:-1])
                line = []
                for i in range(count_dimension):
                    line.append(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write("")
                f.close()
                f = open(file_path, "a")
                str_count_dimension = str(count_dimension - 1) + "\n"
                f.write(str_count_dimension)
                for i in range(count_dimension):
                    if i != int_input - 1:
                        f.write(line [i])
                    else:
                        delete_dimension = line [i][:-1]
                f.close()
                file_path = path.join(commond_path, 'Film', filmname, 'price.txt')
                f = open(file_path, "r")
                line = []
                for i in range(count_dimension):
                    line.append(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write("")
                f.close()
                f = open(file_path, "a")
                for i in range(count_dimension):
                    if i != int_input - 1:
                        f.write(line [i])
                f.close()
                file_path = path.join(commond_path, 'Film', filmname, 'st_price.txt')
                f = open(file_path, "r")
                line = []
                for i in range(count_dimension):
                    line.append(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write("")
                f.close()
                f = open(file_path, "a")
                for i in range(count_dimension):
                    if i != int_input - 1:
                        f.write(line [i])
                f.close()
                file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
                f = open(file_path, "r")
                count_language = int(f.readline() [:-1])
                list_language = []
                for i in range(count_language):
                    list_language.append(f.readline() [:-1])
                f.close()
                list_showing = []
                for i in list_language:
                    file_path = path.join(commond_path, 'Showing', '__Film information', filmname, delete_dimension, i, 'Showingnum.txt')
                    f = open(file_path, "r")
                    count_showing = int(f.readline())
                    f.close()
                    remove(file_path)
                    file_path = path.join(commond_path, 'Showing', '__Film information', filmname, delete_dimension, i, 'Showing.txt')
                    f = open(file_path, "r")
                    for j in range(count_showing):
                        f.readline()
                        list_showing.append(f.readline() [:-1])
                    f.close()
                    remove(file_path)
                    rmdir(path.join(commond_path, 'Showing', '__Film information', filmname, delete_dimension, i))
                rmdir(path.join(commond_path, 'Showing', '__Film information', filmname, delete_dimension))
                file_path = path.join(commond_path, 'House', 'housename.txt')
                f = open(file_path, "r")
                count_house = int(f.readline() [:-1])
                list_house = []
                for j in range(count_house):
                    list_house.append(f.readline() [:-1])
                f.close()
                for i in list_house:
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Showingnum.txt')
                    f = open(file_path, "r")
                    count_showing = int(f.readline())
                    str_count_showing = count_showing
                    f.close()
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Showing.txt')
                    f = open(file_path, "r")
                    g = open(path.join(commond_path, 'Showing', '__House information', i, 'Time.txt'))
                    line = ""
                    line1 = ""
                    for j in range(count_showing):
                        temp1 = f.readline()
                        temp2 = f.readline()
                        temp3 = g.readline()
                        temp4 = g.readline()
                        temp5 = g.readline()
                        if not temp2 [:-1] in list_showing:
                            line += temp1 + temp2
                        else:
                            str_count_showing -= 1
                        if not temp5 [:-1] in list_showing:
                            line1 += temp3 + temp4 + temp5
                    f.close()
                    g.close()
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Showingnum.txt')
                    f = open(file_path, "w")
                    f.write(str(str_count_showing))
                    f.close()
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Showing.txt')
                    f = open(file_path, "w")
                    f.write(line)
                    f.close()
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Time.txt')
                    f = open(file_path, "w")
                    f.write(line1)
                    f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt')
                f = open(file_path, "r")
                count_showing = int(f.readline())
                str_count_showing = count_showing
                f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showing.txt')
                f = open(file_path, "r")
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Time.txt')
                g = open(file_path, "r")
                line = ""
                line1 = ""
                for j in range(count_showing):
                    temp1 = f.readline()
                    temp2 = f.readline()
                    temp3 = g.readline()
                    temp4 = g.readline()
                    temp5 = g.readline()
                    if not temp2 [:-1] in list_showing:
                        line += temp1 + temp2
                    else:
                        str_count_showing -= 1
                    if not temp5 [:-1] in list_showing:
                        line1 += temp3 + temp4 + temp5
                f.close()
                g.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt')
                f = open(file_path, "w")
                f.write(str(str_count_showing))
                f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showing.txt')
                f = open(file_path, "w")
                f.write(line)
                f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Time.txt')
                f = open(file_path, "w")
                f.write(line1)
                f.close()
                for i in list_showing:
                    remove(path.join(commond_path, 'Showing', i, 'film.txt'))
                    remove(path.join(commond_path, 'Showing', i, 'house.txt'))
                    remove(path.join(commond_path, 'Showing', i, 'houseplan.txt'))
                    remove(path.join(commond_path, 'Showing', i, 'starttime.txt'))
                    remove(path.join(commond_path, 'Showing', i, 'ticket.txt'))
                    rmdir(path.join(commond_path, 'Showing', i))
                    file_path = path.join(commond_path, 'Showing', 'Missshowing.txt')
                    f = open(file_path, "a")
                    f.write(i + "\n")
                    f.close()
                    file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
                    f = open(file_path, "r")
                    count_showing = int(f.readline())
                    f.close()
                    file_path = path.join(commond_path, 'Showing', 'Showing.txt')
                    f = open(file_path, "r")
                    line = ""
                    for j in range(count_showing):
                        temp = f.readline()
                        if not temp [:-1] in list_showing:
                            line += temp
                    f.close()
                    file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
                    f = open(file_path, "w")
                    f.write(str(count_showing - 1))
                    f.close()
                    file_path = path.join(commond_path, 'Showing', 'Showing.txt')
                    f = open(file_path, "w")
                    f.write(line)
                    f.close()
                stage = 309
        #film > data > price
        elif stage == 312:
            file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
            f = open(file_path, "r")
            count_price = int(f.readline() [:-1])
            dimension = []
            for i in range(count_price):
                dimension.append(f.readline() [:-1])
            f.close()
            file_path = path.join(commond_path, 'Film', filmname, 'price.txt')
            f = open(file_path, "r")
            line = []
            for i in range(count_price):
                line.append(f.readline() [:-1])
            f.close()
            file_path = path.join(commond_path, 'Film', filmname, 'st_price.txt')
            f = open(file_path, "r")
            line1 = []
            for i in range(count_price):
                line1.append(f.readline() [:-1])
            f.close()
            print(Colour.Underline + filmname + Colour.Reset)
            print("")
            for i in range(count_price):
                print("Current price of {}        : ${}".format(dimension [i], line [i]))
                print("Current student price of {}: ${}".format(dimension [i], line1 [i]))
            print("")
            record = []
            record1 = []
            for i in range(count_price):
                str_input = ""
                while str_input == "":
                    print("New price of {}        : $".format(dimension [i]), end = "")
                    str_input = input("")
                    while str_input != "" and str_input [0] == " ":
                        temp = ""
                        for i in range(1, len(str_input)):
                            temp += str_input [i]
                        str_input = temp
                    while str_input != "" and str_input [len(str_input) - 1] == " ":
                        temp = ""
                        for i in range(0, len(str_input) - 1):
                            temp += str_input [i]
                        str_input = temp
                    if str_input == "":
                        print(Colour.Red + "PRICE CANNOT BE EMPTY" + Colour.Reset)
                        input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                        clearscreen()
                        print(Colour.Underline + filmname + Colour.Reset)
                        print("")
                        for j in range(count_price):
                            print("Current price of {}        : ${}".format(dimension [j], line [j]))
                            print("Current student price of {}: ${}".format(dimension [j], line1 [j]))
                        print("")
                        for j in range(i):
                            print("New price of {}        : ${}".format(dimension [j], record [j]))
                            print("New student price of {}: ${}".format(dimension [j], record1 [j]))
                    elif str_input.isdigit() == False:
                        str_input = ""
                        print(Colour.Red + "PRICE MUST BE INTEGER" + Colour.Reset)
                        input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                        clearscreen()
                        print(Colour.Underline + filmname + Colour.Reset)
                        print("")
                        for j in range(count_price):
                            print("Current price of {}        : ${}".format(dimension [j], line [j]))
                            print("Current student price of {}: ${}".format(dimension [j], line1 [j]))
                        print("")
                        for j in range(i):
                            print("New price of {}        : ${}".format(dimension [j], record [j]))
                            print("New student price of {}: ${}".format(dimension [j], record1 [j]))
                    else:
                        record.append(str_input)
                str_input = ""
                while str_input == "":
                    print("New student price of {}: $".format(dimension [i]), end = "")
                    str_input = input("")
                    while str_input != "" and str_input [0] == " ":
                        temp = ""
                        for i in range(1, len(str_input)):
                            temp += str_input [i]
                        str_input = temp
                    while str_input != "" and str_input [len(str_input) - 1] == " ":
                        temp = ""
                        for i in range(0, len(str_input) - 1):
                            temp += str_input [i]
                        str_input = temp
                    if str_input == "":
                        print(Colour.Red + "STUDENT PRICE CANNOT BE EMPTY" + Colour.Reset)
                        input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                        clearscreen()
                        print(Colour.Underline + filmname + Colour.Reset)
                        print("")
                        for j in range(count_price):
                            print("Current price of {}        : ${}".format(dimension [j], line [j]))
                            print("Current student price of {}: ${}".format(dimension [j], line1 [j]))
                        print("")
                        for j in range(i):
                            print("New price of {}        : ${}".format(dimension [j], record [j]))
                            print("New student price of {}: ${}".format(dimension [j], record1 [j]))
                    elif str_input.isdigit() == False:
                        str_input = ""
                        print(Colour.Red + "PRICE MUST BE INTEGER" + Colour.Reset)
                        input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                        clearscreen()
                        print(Colour.Underline + filmname + Colour.Reset)
                        print("")
                        for j in range(count_price):
                            print("Current price of {}        : ${}".format(dimension [j], line [j]))
                            print("Current student price of {}: ${}".format(dimension [j], line1 [j]))
                        print("")
                        for j in range(i):
                            print("New price of {}        : ${}".format(dimension [j], record [j]))
                            print("New student price of {}: ${}".format(dimension [j], record1 [j]))
                    else:
                        record1.append(str_input)
            price = ""
            for i in range(count_price):
                price = price + record [i] + "\n"
            file_path = path.join(commond_path, 'Film', filmname, 'price.txt')
            f = open(file_path, "w")
            f.write(price)
            f.close()
            st_price = ""
            for i in range(count_price):
                st_price = st_price + record1 [i] + "\n"
            file_path = path.join(commond_path, 'Film', filmname, 'st_price.txt')
            f = open(file_path, "w")
            f.write(st_price)
            f.close()
            stage = 302
        #film > data > deletion
        elif stage == 313:
            int_input = 0
            verification_code = print_313(filmname)
            record = input("")
            if record [0] == verification_code:
                int_input = 1
                file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
                f = open(file_path, "r")
                count_dimension = int(f.readline() [:-1])
                list_dimension = []
                for i in range(count_dimension):
                    list_dimension.append(f.readline() [:-1])
                f.close()
                file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
                f = open(file_path, "r")
                count_language = int(f.readline() [:-1])
                list_language = []
                for i in range(count_language):
                    list_language.append(f.readline() [:-1])
                f.close()
                list_showing = []
                for i in list_dimension:
                    for j in list_language:
                        file_path = path.join(commond_path, 'Showing', '__Film information', filmname, i, j, 'Showingnum.txt')
                        f = open(file_path, "r")
                        count_showing = int(f.readline())
                        f.close()
                        file_path = path.join(commond_path, 'Showing', '__Film information', filmname, i, j, 'Showing.txt')
                        f = open(file_path, "r")
                        for k in range(count_showing):
                            f.readline()
                            list_showing.append(f.readline() [:-1])
                        f.close()
                        file_path = path.join(commond_path, 'Showing', '__Film information', filmname, i, j, 'Showingnum.txt')
                        remove(file_path)
                        file_path = path.join(commond_path, 'Showing', '__Film information', filmname, i, j, 'Showing.txt')
                        remove(file_path)
                        rmdir(path.join(commond_path, 'Showing', '__Film information', filmname, i, j))
                    rmdir(path.join(commond_path, 'Showing', '__Film information', filmname, i))
                rmdir(path.join(commond_path, 'Showing', '__Film information', filmname))
                file_path = path.join(commond_path, 'House', 'housename.txt')
                f = open(file_path, "r")
                count_house = int(f.readline() [:-1])
                list_house = []
                for i in range(count_house):
                    list_house.append(f.readline() [:-1])
                f.close()
                for i in list_house:
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Showingnum.txt')
                    f = open(file_path, "r")
                    count_showing = int(f.readline())
                    str_count_showing = count_showing
                    f.close()
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Showing.txt')
                    f = open(file_path, "r")
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Time.txt')
                    g = open(file_path, "r")
                    line = ""
                    line1 = ""
                    for j in range(count_showing):
                        temp1 = f.readline()
                        temp2 = f.readline()
                        temp3 = f.readline()
                        temp4 = f.readline()
                        temp5 = f.readline()
                        if not temp2 [:-1] in list_showing:
                            line += temp1 + temp2
                        else:
                            str_count_showing -= 1
                        if not temp5 [:-1] in list_showing:
                            line1 += temp3 + temp4 + temp5
                    f.close()
                    g.close()
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Showing.txt')
                    f = open(file_path, "w")
                    f.write(line)
                    f.close()
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Time.txt')
                    f = open(file_path, "w")
                    f.write(line1)
                    f.close()
                    file_path = path.join(commond_path, 'Showing', '__House information', i, 'Showingnum.txt')
                    f = open(file_path, "w")
                    f.write(str(str_count_showing))
                    f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt')
                f = open(file_path, "r")
                count_showing = int(f.readline())
                str_count_showing = count_showing
                f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showing.txt')
                f = open(file_path, "r")
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Time.txt')
                g = open(file_path, "r")
                line = ""
                line1 = ""
                for j in range(count_showing):
                    temp1 = f.readline()
                    temp2 = f.readline()
                    temp3 = f.readline()
                    temp4 = f.readline()
                    temp5 = f.readline()
                    if not temp2 [:-1] in list_showing:
                        line += temp1 + temp2
                    else:
                        str_count_showing -= 1
                    if not temp5 [:-1] in list_showing:
                        line1 += temp3 + temp4 + temp5
                f.close()
                g.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showing.txt')
                f = open(file_path, "w")
                f.write(line)
                f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Time.txt')
                f = open(file_path, "w")
                f.write(line1)
                f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt')
                f = open(file_path, "w")
                f.write(str(str_count_showing))
                f.close()
                file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
                f = open(file_path, "r")
                count_showing = int(f.readline())
                f.close()
                file_path = path.join(commond_path, 'Showing', 'Showing.txt')
                f = open(file_path, "r")
                line = ""
                for j in range(count_showing):
                    temp = f.readline()
                    if not temp [:-1] in list_showing:
                        line += temp
                f.close()
                f = open(file_path, "w")
                f.write(line)
                f.close()
                for i in list_showing:
                    file_path = path.join(commond_path, 'Showing', 'Missshowing.txt')
                    f = open(file_path, "a")
                    f.write(i + "\n")
                    f.close()
                    file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
                    f = open(file_path, "r")
                    count_showing = int(f.readline())
                    f.close()
                    f = open(file_path, "w")
                    f.write(str(count_showing - 1))
                    f.close()
                    file_path = path.join(commond_path, 'Showing', i, 'film.txt')
                    remove(file_path)
                    file_path = path.join(commond_path, 'Showing', i, 'house.txt')
                    remove(file_path)
                    file_path = path.join(commond_path, 'Showing', i, 'houseplan.txt')
                    remove(file_path)
                    file_path = path.join(commond_path, 'Showing', i, 'starttime.txt')
                    remove(file_path)
                    file_path = path.join(commond_path, 'Showing', i, 'ticket.txt')
                    remove(file_path)
                    file_path = path.join(commond_path, 'Showing', i)
                    rmdir(file_path)
                file_path = path.join(commond_path, 'Film', 'filmname.txt')
                line = []
                f = open(file_path, "r")
                count_film = int(f.readline() [:-1])
                for i in range(count_film):
                    line.append(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write("")
                f.close()
                f = open(file_path, "a")
                f.write(str(count_film - 1) + "\n")
                for i in range(count_film):
                    if line [i] != filmname + "\n":
                        f.write(line [i])
                f.close()
                file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
                remove(file_path)
                file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
                remove(file_path)
                file_path = path.join(commond_path, 'Film', filmname, 'price.txt')
                remove(file_path)
                file_path = path.join(commond_path, 'Film', filmname, 'st_price.txt')
                remove(file_path)
                file_path = path.join(commond_path, 'Film', filmname, 'rating.txt')
                remove(file_path)
                file_path = path.join(commond_path, 'Film', filmname, 'timelength.txt')
                remove(file_path)
                rmdir(path.join(commond_path, 'Film', filmname))
            if int_input == 0:
                stage = 302
            else:
                stage = 301
        #film > addition
        elif stage == 314:
            name = ""
            while name == "":
                clearscreen()
                name = input("What is the name of the film: ")
                while name != "" and name [0] == " ":
                    temp = ""
                    for i in range(1, len(name)):
                        temp += name [i]
                    name = temp
                while name != "" and name [len(name) - 1] == " ":
                    temp = ""
                    for i in range(0, len(name) - 1):
                        temp += name [i]
                    name = temp
                if name == "":
                    print(Colour.Red + "FILM NAME CANNOT BE EMPTY" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif file_name_include(name) == False:
                    name = ""
                    print(Colour.Red + "FILM NAME CANNOT INCLUDE \/:*?\"<>|" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif name.upper() == "Film addition".upper():
                    name = ""
                    print(Colour.Red + "FILM NAME CANNOT BE \"Film addition\"" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif name.upper() == "Go back".upper():
                    name = ""
                    print(Colour.Red + "FILM NAME CANNOT BE \"Go back\"" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                elif file_name_include_ascii(name) == False:
                    name = ""
                    print(Colour.Red + "FILM NAME MUST BE WITHIN ASCII 32 to 126" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                file_path = path.join(commond_path, 'Film', 'filmname.txt')
                f = open(file_path, "r")
                count_film = int(f.readline() [:-1])
                line = []
                for i in range(count_film):
                    line.append(f.readline() [:-1])
                    if line [i].upper() == name.upper():
                        name = ""
                        print(Colour.Red + "FILM NAME CANNOT BE THE SAME AS OTHER FILMS" + Colour.Reset)
                        input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                f.close()
            f = open(file_path, "w")
            f.write("")
            f.close()
            f = open(file_path, "a")
            f.write(str(count_film + 1) + "\n")
            for i in range(count_film):
                f.write(line [i] + "\n")
            f.write(name + "\n")
            f.close()
            if not path.exists(path.join(commond_path, 'Film', name)):
                mkdir(path.join(commond_path, 'Film', name))
            file_path = path.join(commond_path, 'Film', name, 'dimension.txt')
            f = open(file_path, "w")
            f.write("1\n2D\n")
            f.close()
            file_path = path.join(commond_path, 'Film', name, 'language.txt')
            f = open(file_path, "w")
            f.write("1\nEnglish\n")
            f.close()
            file_path = path.join(commond_path, 'Film', name, 'price.txt')
            f = open(file_path, "w")
            f.write("0\n")
            f.close()
            file_path = path.join(commond_path, 'Film', name, 'st_price.txt')
            f = open(file_path, "w")
            f.write("0\n")
            f.close()
            file_path = path.join(commond_path, 'Film', name, 'rating.txt')
            f = open(file_path, "w")
            f.write("I")
            f.close()
            file_path = path.join(commond_path, 'Film', name, 'timelength.txt')
            f = open(file_path, "w")
            f.write("100")
            f.close()
            if not path.exists(path.join(commond_path, 'Showing', '__Film information', name)):
                mkdir(path.join(commond_path, 'Showing', '__Film information', name))
            if not path.exists(path.join(commond_path, 'Showing', '__Film information', name, '2D')):
                mkdir(path.join(commond_path, 'Showing', '__Film information', name, '2D'))
            if not path.exists(path.join(commond_path, 'Showing', '__Film information', name, '2D', 'English')):
                mkdir(path.join(commond_path, 'Showing', '__Film information', name, '2D', 'English'))
            file_path = path.join(commond_path, 'Showing', '__Film information', name, '2D', 'English', 'Showing.txt')
            f = open(file_path, "w")
            f.write("")
            f.close()
            file_path = path.join(commond_path, 'Showing', '__Film information', name, '2D', 'English', 'Showingnum.txt')
            f = open(file_path, "w")
            f.write("0")
            f.close()
            filmname_accord()
            filmname = name
            stage = 302
        #showing
        elif stage == 401:
            last_stage = 401
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_401()
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 1
            elif int_input == 1:
                stage = 402
            elif int_input == 2:
                stage = 407
            elif int_input == 3:
                stage = 410
            elif int_input == 4:
                stage = 412
            elif int_input == 5:
                stage = 424
        #showing > film
        elif stage == 402:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_402()
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 401
            else:
                file_path = path.join(commond_path, 'Film', 'filmname.txt')
                f = open(file_path, "r")
                for i in range(int_input):
                    f.readline()
                filmname = f.readline() [:-1]
                f.close()
                stage = 403
        #showing > film > dimension
        elif stage == 403:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_403(filmname)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 402
            else:
                file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
                f = open(file_path, "r")
                for i in range(int_input):
                    f.readline()
                dimension = f.readline() [:-1]
                f.close()
                stage = 404
        #showing > film > dimension > language
        elif stage == 404:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_404(filmname, dimension)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 403
            else:
                file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
                f = open(file_path, "r")
                for i in range(int_input):
                    f.readline() 
                language = f.readline() [:-1]
                f.close()
                stage = 405
        #showing > film > dimension > language > time
        elif stage == 405:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_405(filmname, dimension, language)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 404
            else:
                if int_input == 1:
                    time = "previous"
                elif int_input == 2:
                    time = "playing"
                else:
                    time = "upcoming"
                stage = 406
        #showing > film > dimension > language > time > list
        elif stage == 406:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_406(filmname, dimension, language, time)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 405
            else:
                file_path = path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showingnum.txt')
                f = open(file_path, "r")
                sum_showing = int(f.readline())
                f.close()
                showing_list = []
                file_path = path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showing.txt')
                f = open(file_path, "r")
                for i in range(sum_showing):
                    if f.readline() [:-1] == time:
                        showing_list.append(f.readline() [:-1])
                    else:
                        f.readline()
                f.close()
                showing = showing_list [int_input - 1]
                last_stage = 406
                stage = 413
        #showing > house
        elif stage == 407:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_407()
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 401
            else:
                file_path = path.join(commond_path, 'House', 'housename.txt')
                f = open(file_path, "r")
                for i in range(int_input):
                    f.readline()
                house = f.readline() [:-1]
                f.close()
                stage = 408
        #showing > house > time
        elif stage == 408:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_408(house)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 407
            else:
                if int_input == 1:
                    time = "previous"
                elif int_input == 2:
                    time = "playing"
                else:
                    time = "upcoming"
                stage = 409
        #showing > house > time > list
        elif stage == 409:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_409(house, time)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 408
            else:
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showingnum.txt')
                f = open(file_path, "r")
                sum_showing = int(f.readline())
                f.close()
                showing_list = []
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showing.txt')
                f = open(file_path, "r")
                for i in range(sum_showing):
                    if f.readline() [:-1] == time:
                        showing_list.append(f.readline() [:-1])
                    else:
                        f.readline()
                f.close()
                showing = showing_list [int_input - 1]
                last_stage = 409
                stage = 413
        #showing > time
        elif stage == 410:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_410()
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == 1:
                time = "previous"
                stage = 411
            elif int_input == 2:
                time = "playing"
                stage = 411
            elif int_input == 3:
                time = "upcoming"
                stage = 411
            else:
                stage = 401
        #showing > time > list
        elif stage == 411:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_411(time)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 410
            else:
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt')
                f = open(file_path, "r")
                sum_showing = int(f.readline())
                f.close()
                count_showing = 0
                showing_list = []
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showing.txt')
                f = open(file_path, "r")
                for i in range(sum_showing):
                    if f.readline() [:-1] == time:
                        count_showing += 1
                        showing_list.append(f.readline() [:-1])
                    else:
                        f.readline()
                f.close()
                showing = showing_list [int_input - 1]
                last_stage = 411
                stage = 413
        #showing > search
        elif stage == 412:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_412()
                int_input = input_int_check("Input number: ", choose)
                file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
            if int_input == choose:
                stage = 401
            else:
                f = open(file_path, "r")
                count_showing = int(f.readline())
                f.close()
                file_path = path.join(commond_path, 'Showing', 'Showing.txt')
                f = open(file_path, "r")
                showing = []
                for i in range(count_showing):
                    showing.append(f.readline() [:-1])
                f.close()
                missshowing = []
                file_path = path.join(commond_path, 'Showing', 'Missshowing.txt')
                f = open(file_path, "r")
                while True:
                    line = f.readline() [:-1]
                    if line == "":
                        break
                    else:
                        count_showing += 1
                        missshowing.append(line)
                        showing.append(line)
                f.close()
                len_count_showing = len(str(count_showing + 1))
                for i in range(count_showing):
                    for j in range(i + 1, count_showing):
                        if showing [j - 1] >= showing [j]:
                            temp = showing [j - 1]
                            showing [j - 1] = showing [j]
                            showing [j] = temp
                error = 0
                for j in missshowing:
                    if showing [int_input - 1] == j:
                        error = 1
                if error == 1:
                    print(Colour.Red + "THE SHOWING IS DELETED" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO CONTINUE" + Colour.Reset)
                else:
                    showing = showing [int_input - 1]
                    last_stage = 412
                    stage = 413
        #showing > check
        elif stage == 413:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_413(showing)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == 1:
                stage = 414
            elif int_input == 2:
                stage = 415
            elif int_input == 3:
                stage = 416
            elif int_input == 4:
                stage = 417
            elif int_input == 5:
                stage = 418
            elif int_input == 6:
                stage = 423
            else:
                stage = last_stage
        #showing > check > film
        elif stage == 414:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_414(showing, "", "", 0)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 413
            else:
                file_path = path.join(commond_path, 'Showing', showing, 'film.txt')
                f = open(file_path, "r")
                filmname = f.readline() [:-1]
                f.close()
                file_path = path.join(commond_path, 'Film', 'filmname.txt')
                f = open(file_path, "r")
                film_list = []
                film_count = int(f.readline() [:-1])
                for i in range(film_count):
                    film_list.append(f.readline() [:-1])
                    if film_list [i] == filmname:
                        film_list [i] = ""
                f.close()
                for i in range(film_count):
                    if film_list [i] == "":
                        temp = i
                del film_list [temp]
                filmname = film_list [int_input - 1]
                int_input = 0
                choose = 0
                while int_input == 0 or int_input > choose:
                    choose = print_414(showing, filmname, "", 1)
                    int_input = input_int_check("Input number: ", choose)
                    clearscreen()
                if int_input == choose:
                    stage = 413
                else:
                    file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
                    f = open(file_path, "r")
                    dimension_list = []
                    dimension_count = int(f.readline() [:-1])
                    for i in range(dimension_count):
                        dimension_list.append(f.readline() [:-1])
                    f.close()
                    dimension = dimension_list [int_input - 1]
                    int_input = 0
                    choose = 0
                    while int_input == 0 or int_input > choose:
                        choose = print_414(showing, filmname, dimension, 2)
                        int_input = input_int_check("Input number: ", choose)
                        clearscreen()
                    if int_input == choose:
                        stage = 413
                    else:
                        file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
                        f = open(file_path, "r")
                        language_list = []
                        language_count = int(f.readline() [:-1])
                        for i in range(language_count):
                            language_list.append(f.readline() [:-1])
                        f.close()
                        language = language_list [int_input - 1]
                        file_path = path.join(commond_path, 'Showing', showing, 'film.txt')
                        f = open(file_path, "w")
                        f.write(filmname + "\n" + dimension + "\n" + language + "\n")
                        f.close()
                        stage = 413
        #showing > check > dimension
        elif stage == 415:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_415(showing)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 413
            else:
                file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
                f = open(file_path, "r")
                dimension_list = []
                dimension_count = int(f.readline() [:-1])
                for i in range(dimension_count):
                    dimension_list.append(f.readline() [:-1])
                f.close()
                for i in range(dimension_count - 1, -1, -1):
                    if dimension_list [i] == dimension:
                        del dimension_list [i]
                dimension = dimension_list [int_input - 1]
                file_path = path.join(commond_path, 'Showing', showing, 'film.txt')
                f = open(file_path, "r")
                line = []
                line.append(f.readline())
                f.readline()
                line.append(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write(line [0] + dimension + "\n" + line [1])
                f.close()
                stage = 413
        #showing > check > language
        elif stage == 416:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_416(showing)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 413
            else:
                file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
                f = open(file_path, "r")
                language_list = []
                language_count = int(f.readline() [:-1])
                for i in range(language_count):
                    language_list.append(f.readline() [:-1])
                f.close()
                for i in range(language_count - 1, -1, -1):
                    if language_list [i] == language:
                        del language_list [i]
                language = language_list [int_input - 1]
                file_path = path.join(commond_path, 'Showing', showing, 'film.txt')
                f = open(file_path, "r")
                line = []
                line.append(f.readline())
                line.append(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write(line [0] + line [1] + language + "\n")
                f.close()
                stage = 413
        #showing > check > time
        elif stage == 417:
            str_input = ""
            exit_input = 0
            while str_input == "" and exit_input == 0:
                clearscreen()
                print_417(showing)
                str_input = input("Input new starting time (follow the format): ")
                while str_input != "" and str_input [0] == " ":
                    temp = ""
                    for i in range(1, len(str_input)):
                        temp += str_input [i]
                    str_input = temp
                while str_input != "" and str_input [len(str_input) - 1] == " ":
                    temp = ""
                    for i in range(0, len(str_input) - 1):
                        temp += str_input [i]
                    str_input = temp
                if str_input == "exit" or str_input == "Exit" or str_input == "EXIT":
                    exit_input = 1
                else:
                    if str_input == "":
                        print(Colour.Red + "INPUT CANNOT BE EMPTY" + Colour.Reset)
                        input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                    else:
                        if len(str_input) == 17:
                            str_input1 = str_input [0] + str_input [1]
                            str_input2 = str_input [3] + str_input [4]
                            str_input3 = str_input [6] + str_input [7]
                            str_input4 = str_input [9] + str_input [10]
                            str_input5 = str_input [12] + str_input [13]
                            str_input6 = str_input [15] + str_input [16]
                            if str_input1.isdecimal() and str_input2.isdecimal() and str_input3.isdecimal() and str_input4.isdecimal() and str_input5.isdecimal() and str_input6.isdecimal() and str_input [2] == "/" and str_input [5] == "/" and str_input [8] == " " and str_input [11] == ":" and str_input [14] == ":":
                                if int(str_input2) != 0 and int(str_input2) <= 12 and int(str_input4) <= 23 and int(str_input5) <= 59 and int(str_input6) <=59:
                                    if int(str_input2) == 1 or int(str_input2) == 3 or int(str_input2) == 5 or int(str_input2) == 7 or int(str_input2) == 8 or int(str_input2) == 10 or int(str_input2) == 12:
                                        if int(str_input1) > 31 and int(str_input1) != 0:
                                            str_input = ""
                                            print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                    elif int(str_input2) == 2:
                                        temp = int(str_input3)
                                        while temp > 0:
                                            temp -= 4
                                        if temp == 0:
                                            if int(str_input1) > 29 and int(str_input1) != 0:
                                                str_input = ""
                                                print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                                input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                        else:
                                            if int(str_input1) > 28 and int(str_input1) != 0:
                                                str_input = ""
                                                print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                                input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                    else:
                                        if int(str_input1) > 30 and int(str_input1) != 0:
                                            str_input = ""
                                            print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                else:
                                    str_input = ""
                                    print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                            else:
                                str_input = ""
                                print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                        else:
                            str_input = ""
                            print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
            if exit_input == 0:
                file_path = path.join(commond_path, 'Showing', showing, 'starttime.txt')
                f = open(file_path, "w")
                f.write(str_input)
                f.close()
                stage = 413
            else:
                stage = 413
        #showing > check > house
        elif stage == 418:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_418(showing)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 413
            elif int_input == choose - 1:
                stage = 419
            else:
                file_path = path.join(commond_path, 'Showing', showing, 'ticket.txt')
                f = open(file_path, "r")
                ticket_list = []
                while True:
                    temp = f.readline()
                    if temp == "":
                        break
                    else:
                        ticket_list.append(temp [:-1])
                f.close()
                ticket = ticket_list [int_input - 1]
                stage = 420
        #showing > check > house > change
        elif stage == 419:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_419(showing)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 413
            else:
                file_path = path.join(commond_path, 'Showing', showing, 'house.txt')
                f = open(file_path, "r")
                house = f.readline()
                f.close()
                file_path = path.join(commond_path, 'House', 'housename.txt')
                f = open(file_path, "r")
                house_count = int(f.readline() [:-1])
                house_list = []
                for i in range(house_count):
                    temp = f.readline() [:-1]
                    if temp != house:
                        house_list.append(temp)
                f.close()
                house = house_list [int_input - 1]
                file_path = path.join(commond_path, 'Showing', showing, 'house.txt')
                f = open(file_path, "w")
                f.write(house)
                f.close()
                file_path = path.join(commond_path, 'House', house, 'houseplan.txt')
                f = open(file_path, "r")
                houseplan = f.read()
                f.close()
                file_path = path.join(commond_path, 'Showing', showing, 'houseplan.txt')
                f = open(file_path, "w")
                f.write(houseplan)
                f.close()
                file_path = path.join(commond_path, 'Showing', showing, 'ticket.txt')
                f = open(file_path, "w")
                f.write("")
                f.close()
                stage = 418
        #showing > check > house > ticket
        elif stage == 420:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_420(showing, ticket)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 418
            elif int_input == 1:
                stage = 421
            else:
                stage = 422
        #showing > check > house > ticket > changeseat
        elif stage == 421:
            column_ticket = ticket [11:-1]
            while not column_ticket.isdecimal():
                column_ticket = column_ticket [1:]
            column_ticket_record = column_ticket
            column_ticket = int(column_ticket) - 1
            row_ticket = ticket [11:-1]
            for i in range(len(str(column_ticket + 1))):
                row_ticket = row_ticket [:-1]
            row_ticket_record = row_ticket
            row_ticket = eng_to_int(row_ticket)
            file_path = path.join(commond_path, 'Showing', showing, 'houseplan.txt')
            f = open(file_path, "r")
            seating_plan = []
            row = 0
            while True:
                line = f.readline()
                if line == "":
                    break
                else:
                    row += 1
                    temp = []
                    i = 0
                    while True:
                        if line [i] == "\n":
                            break
                        else:
                            column = len(line [:-1])
                            temp.append(line [i])
                            i += 1
                    seating_plan.append(temp)
            f.close()
            row_record = ""
            row_input = ""
            column_input = ""
            exit_input = 0
            while row_input == "" and column_input == "" and exit_input == 0:
                clearscreen()
                print_plan(showing, "", row_ticket, column_ticket, 3)
                print("")
                print(Colour.Underline + "Status of seats" + Colour.Reset + ":")
                print(Colour.Green + "O" + Colour.Reset + " <-> Available seats")
                print(Colour.Red + "X" + Colour.Reset + " <-> Sold seats")
                print(Colour.Blue + "\ua554" + Colour.Reset + " <-> Unavailable seats")
                print("")
                print("Input \"exit\" to exit")
                print("")
                row_input = input("Input the new row of ticket: ")
                row_record = row_input
                while row_input != "" and row_input [0] == " ":
                    temp = ""
                    for i in range(1, len(row_input)):
                        temp += row_input [i]
                    row_input = temp
                while row_input != "" and row_input [len(row_input) - 1] == " ":
                    temp = ""
                    for i in range(0, len(row_input) - 1):
                        temp += row_input [i]
                    row_input = temp
                if row_input == "exit" or row_input == "Exit" or row_input == "EXIT":
                    exit_input = 1
                else:
                    if row_input == "":
                        print(Colour.Red + "INPUT CANNOT BE EMPTY" + Colour.Reset)
                        input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                    else:
                        row_input = eng_to_int(row_input)
                        if row_input == -1 or row_input >= row:
                            row_input = ""
                            print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                        else:
                            clearscreen()
                            print_plan(showing, "", row_ticket, column_ticket, 3)
                            print("Input \"exit\" to exit")
                            print("")
                            print("Input the new row of ticket: " + row_record)
                            column_input = input("Input the new column of ticket: ")
                            column_record = column_input
                            while column_input != "" and column_input [0] == " ":
                                temp = ""
                                for i in range(1, len(column_input)):
                                    temp += column_input [i]
                                column_input = temp
                            while column_input != "" and column_input [len(column_input) - 1] == " ":
                                temp = ""
                                for i in range(0, len(column_input) - 1):
                                    temp += column_input [i]
                                column_input = temp
                            if column_input == "exit" or column_input == "Exit" or column_input == "EXIT":
                                exit_input = 1
                            else:
                                if column_input == "":
                                    row_input = ""
                                    print(Colour.Red + "INPUT CANNOT BE EMPTY" + Colour.Reset)
                                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                else:
                                    if column_input.isdecimal():
                                        column_input = int(column_input)
                                        if column_input > 0 and column_input <= column:
                                            column_input -= 1
                                            if seating_plan [row_input][column_input] == "0":
                                                new_seating_plan = ""
                                                for i in range(row):
                                                    for j in range(column):
                                                        if i == row_ticket and j == column_ticket:
                                                            new_seating_plan += "0"
                                                        elif i == row_input and j == column_input:
                                                            new_seating_plan += "1"
                                                        else:
                                                            new_seating_plan += seating_plan [i][j]
                                                    new_seating_plan += "\n"
                                                file_path = path.join(commond_path, 'Showing', showing, 'houseplan.txt')
                                                f = open(file_path, "w")
                                                f.write(new_seating_plan)
                                                f.close()
                                                file_path = path.join(commond_path, 'Showing', showing, 'ticket.txt')
                                                f = open(file_path, "r")
                                                string_ticket = ""
                                                while True:
                                                    line = f.readline()
                                                    if line == "":
                                                        break
                                                    else:
                                                        if line [11:-2] == row_ticket_record + column_ticket_record:
                                                            while line [1] != "\n":
                                                                line = line [1:]
                                                            string_ticket += "T" + showing [1:] + row_record.upper() + column_record + line
                                                            ticket = "T" + showing [1:] + row_record.upper() + column_record + line [:-1]
                                                        else:
                                                            string_ticket += line
                                                f.close()
                                                f = open(file_path, "w")
                                                f.write(string_ticket)
                                                f.close()
                                                ticket_accord()
                                            else:
                                                row_input = ""
                                                column_input = ""
                                                print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                                input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                        else:
                                            row_input = ""
                                            column_input = ""
                                            print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                    else:
                                        row_input = ""
                                        column_input = ""
                                        print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                        input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
            stage = 420
        #showing > check > house > ticket > delete
        elif stage == 422:
            int_input = 0
            verification_code = print_422(ticket)
            record = input("")
            if record == verification_code:
                int_input = 1
            if int_input == 0:
                stage = 420
            else:
                stage = 418
                file_path = path.join(commond_path, 'Showing', showing, 'ticket.txt')
                list_ticket = []
                str_ticket = ""
                f = open(file_path, "r")
                while True:
                    line = f.readline() [:-1]
                    if line == "":
                        break
                    else:
                        if line != ticket:
                            str_ticket += line + "\n"
                            list_ticket.append(line)
                f.close()
                f = open(file_path, "w")
                f.write(str_ticket)
                f.close()
                column_ticket = ticket [11:-1]
                while not column_ticket.isdecimal():
                    column_ticket = column_ticket [1:]
                column_ticket = int(column_ticket) - 1
                row_ticket = ticket [11:-1]
                for i in range(len(str(column_ticket + 1))):
                    row_ticket = row_ticket [:-1]
                row_ticket = eng_to_int(row_ticket)
                file_path = path.join(commond_path, 'Showing', showing, 'houseplan.txt')
                f = open(file_path, "r")
                seating_plan = ""
                row = 0
                while True:
                    line = f.readline()
                    if line == "":
                        break
                    else:
                        row += 1
                        column = len(line [:-1])
                        if row == row_ticket + 1:
                            for i in range(column + 1):
                                if i == column_ticket:
                                    seating_plan += "0"
                                else:
                                    seating_plan += line [i]
                        else:
                            seating_plan += line
                f.close()
                f = open(file_path, "w")
                f.write(seating_plan)
                f.close()
        #showing > check > delete
        elif stage == 423:
            int_input = 0
            verification_code = print_423(showing)
            record = input("")
            if record == verification_code:
                int_input = 1
            if int_input == 0:
                stage = 413
            else:
                file_path = path.join(commond_path, 'Showing', showing, 'film.txt')
                f = open(file_path, "r")
                filmname = f.readline() [:-1]
                dimension = f.readline() [:-1]
                language = f.readline() [:-1]
                f.close()
                file_path = path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showingnum.txt')
                f = open(file_path, "r")
                count_showing = int(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write(str(count_showing - 1))
                f.close()
                file_path = path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showing.txt')
                str_lines = ""
                f = open(file_path, "r")
                for i in range(count_showing):
                    line1 = f.readline()
                    line2 = f.readline()
                    if line2 [:-1] != showing:
                        str_lines += line1 + line2
                f.close()
                f = open(file_path, "w")
                f.write(str_lines)
                f.close()
                file_path = path.join(commond_path, 'Showing', showing, 'house.txt')
                f = open(file_path, "r")
                house = f.readline()
                f.close()
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showingnum.txt')
                f = open(file_path, "r")
                count_showing = int(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write(str(count_showing - 1))
                f.close()
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showing.txt')
                str_lines = ""
                f = open(file_path, "r")
                for i in range(count_showing):
                    line1 = f.readline()
                    line2 = f.readline()
                    if line2 [:-1] != showing:
                        str_lines += line1 + line2
                f.close()
                f = open(file_path, "w")
                f.write(str_lines)
                f.close()
                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Time.txt')
                str_lines = ""
                f = open(file_path, "r")
                for i in range(count_showing):
                    line1 = f.readline()
                    line2 = f.readline()
                    line3 = f.readline()
                    if line3 [:-1] != showing:
                        str_lines += line1 + line2 + line3
                f.close()
                f = open(file_path, "w")
                f.write(str_lines)
                f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt')
                f = open(file_path, "r")
                count_showing = int(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write(str(count_showing - 1))
                f.close()
                file_path = path.join(commond_path, 'Showing', '__Time information', 'Showing.txt')
                str_lines = ""
                f = open(file_path, "r")
                for i in range(count_showing):
                    line1 = f.readline()
                    line2 = f.readline()
                    if line2 [:-1] != showing:
                        str_lines += line1 + line2
                f.close()
                f = open(file_path, "w")
                f.write(str_lines)
                f.close()
                file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
                f = open(file_path, "r")
                count_showing = int(f.readline())
                f.close()
                f = open(file_path, "w")
                f.write(str(count_showing - 1))
                f.close()
                file_path = path.join(commond_path, 'Showing', 'Showing.txt')
                str_lines = ""
                f = open(file_path, "r")
                for i in range(count_showing):
                    line = f.readline()
                    if line [:-1] != showing:
                        str_lines += line
                f.close()
                f = open(file_path, "w")
                f.write(str_lines)
                f.close()
                file_path = path.join(commond_path, 'Showing', 'Missshowing.txt')
                f = open(file_path, "a")
                f.write(showing + "\n")
                f.close()
                file_path = path.join(commond_path, 'Showing', showing, 'film.txt')
                remove(file_path)
                file_path = path.join(commond_path, 'Showing', showing, 'house.txt')
                remove(file_path)
                file_path = path.join(commond_path, 'Showing', showing, 'houseplan.txt')
                remove(file_path)
                file_path = path.join(commond_path, 'Showing', showing, 'starttime.txt')
                remove(file_path)
                file_path = path.join(commond_path, 'Showing', showing, 'ticket.txt')
                remove(file_path)
                rmdir(path.join(commond_path, 'Showing', showing))
                stage = 401
        #showing > addition (film > dimension > language > house > starttime)
        elif stage == 424:
            int_input = 0
            choose = 0
            while int_input == 0 or int_input > choose:
                choose = print_424(0, "", "", "", "")
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input == choose:
                stage = 401
            else:
                file_path = path.join(commond_path, 'Film', 'filmname.txt')
                f = open(file_path, "r")
                for i in range(int_input):
                    f.readline()
                filmname = f.readline() [:-1]
                f.close()
                int_input = 0
                choose = 0
                while int_input == 0 or int_input > choose:
                    choose = print_424(1, filmname, "", "", "")
                    int_input = input_int_check("Input number: ", choose)
                    clearscreen()
                if int_input == choose:
                    stage = 401
                else:
                    file_path = path.join(commond_path, 'Film', filmname, 'dimension.txt')
                    f = open(file_path, "r")
                    for i in range(int_input):
                        f.readline()
                    dimension = f.readline() [:-1]
                    f.close()
                    int_input = 0
                    choose = 0
                    while int_input == 0 or int_input > choose:
                        choose = print_424(2, filmname, dimension, "", "")
                        int_input = input_int_check("Input number: ", choose)
                        clearscreen()
                    if int_input == choose:
                        stage = 401
                    else:
                        file_path = path.join(commond_path, 'Film', filmname, 'language.txt')
                        f = open(file_path, "r")
                        for i in range(int_input):
                            f.readline()
                        language = f.readline() [:-1]
                        f.close()
                        int_input = 0
                        choose = 0
                        while int_input == 0 or int_input > choose:
                            choose = print_424(3, filmname, dimension, language, "")
                            int_input = input_int_check("Input number: ", choose)
                            clearscreen()
                        if int_input == choose:
                            stage = 401
                        else:
                            file_path = path.join(commond_path, 'House', 'housename.txt')
                            f = open(file_path, "r")
                            for i in range(int_input):
                                f.readline()
                            house = f.readline() [:-1]
                            f.close()
                            str_input = ""
                            exit_input = 0
                            while str_input == "" and exit_input == 0:
                                clearscreen()
                                showing = print_424(4, filmname, dimension, language, house)
                                str_input = input("Input starting time (follow the format): ")
                                while str_input != "" and str_input [0] == " ":
                                    temp = ""
                                    for i in range(1, len(str_input)):
                                        temp += str_input [i]
                                    str_input = temp
                                while str_input != "" and str_input [len(str_input) - 1] == " ":
                                    temp = ""
                                    for i in range(0, len(str_input) - 1):
                                        temp += str_input [i]
                                    str_input = temp
                                if str_input == "exit" or str_input == "Exit" or str_input == "EXIT":
                                    exit_input = 1
                                else:
                                    if str_input == "":
                                        print(Colour.Red + "INPUT CANNOT BE EMPTY" + Colour.Reset)
                                        input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                    else:
                                        if len(str_input) == 17:
                                            str_input1 = str_input [0] + str_input [1]
                                            str_input2 = str_input [3] + str_input [4]
                                            str_input3 = str_input [6] + str_input [7]
                                            str_input4 = str_input [9] + str_input [10]
                                            str_input5 = str_input [12] + str_input [13]
                                            str_input6 = str_input [15] + str_input [16]
                                            if str_input1.isdecimal() and str_input2.isdecimal() and str_input3.isdecimal() and str_input4.isdecimal() and str_input5.isdecimal() and str_input6.isdecimal() and str_input [2] == "/" and str_input [5] == "/" and str_input [8] == " " and str_input [11] == ":" and str_input [14] == ":":
                                                if int(str_input2) != 0 and int(str_input2) <= 12 and int(str_input4) <= 23 and int(str_input5) <= 59 and int(str_input6) <=59:
                                                    if int(str_input2) == 1 or int(str_input2) == 3 or int(str_input2) == 5 or int(str_input2) == 7 or int(str_input2) == 8 or int(str_input2) == 10 or int(str_input2) == 12:
                                                        if int(str_input1) > 31 and int(str_input1) != 0:
                                                            str_input = ""
                                                            print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                                    elif int(str_input2) == 2:
                                                        temp = int(str_input3)
                                                        while temp > 0:
                                                            temp -= 4
                                                        if temp == 0:
                                                            if int(str_input1) > 29 and int(str_input1) != 0:
                                                                str_input = ""
                                                                print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                                                input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                                        else:
                                                            if int(str_input1) > 28 and int(str_input1) != 0:
                                                                str_input = ""
                                                                print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                                                input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                                    else:
                                                        if int(str_input1) > 30 and int(str_input1) != 0:
                                                            str_input = ""
                                                            print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                                else:
                                                    str_input = ""
                                                    print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                                    input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                            else:
                                                str_input = ""
                                                print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                                input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                        else:
                                            str_input = ""
                                            print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                            if exit_input == 0:
                                file_path = path.join(commond_path, 'Film', filmname, 'timelength.txt')
                                f = open(file_path, "r")
                                timelength = int(f.readline())
                                f.close()
                                format_time = "%d/%m/%y %H:%M:%S"
                                start_time_input = datetime.strptime(str_input, format_time)
                                end_time_input = start_time_input + timedelta(minutes = timelength)
                                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showingnum.txt')
                                f = open(file_path, "r")
                                count_showing_time = int(f.readline())
                                f.close()
                                file_path = path.join(commond_path, 'Showing', '__House information', house, 'Time.txt')
                                f = open(file_path, "r")
                                start_time = []
                                end_time = []
                                showing_time = []
                                timelength_time = []
                                for i in range(count_showing_time):
                                    line1 = f.readline() [:-1]
                                    line2 = int(f.readline() [:-1])
                                    line3 = f.readline() [:-1]
                                    start_time.append(datetime.strptime(line1, format_time))
                                    timelength_time.append(str(line2))
                                    end_time.append(datetime.strptime(line1, format_time) + timedelta(minutes = line2))
                                    showing_time.append(line3)
                                f.close()
                                start_time.append(start_time_input)
                                end_time.append(end_time_input)
                                showing_time.append(showing)
                                timelength_time.append(str(timelength))
                                for i in range(count_showing_time):
                                    for j in range(count_showing_time - i):
                                        if start_time [j] > start_time [j + 1]:
                                            temp = start_time [j]
                                            start_time [j] = start_time [j + 1]
                                            start_time [j + 1] = temp
                                            temp = end_time [j]
                                            end_time [j] = end_time [j + 1]
                                            end_time [j + 1] = temp
                                            temp = showing_time [j]
                                            showing_time [j] = showing_time [j + 1]
                                            showing_time [j + 1] = temp
                                            temp = timelength_time [j]
                                            timelength_time [j] = timelength_time [j + 1]
                                            timelength_time [j + 1] = temp
                                error = 0
                                for i in range(count_showing_time):
                                    if start_time [i] <= start_time [i + 1] and end_time [i] > start_time [i + 1] and error == 0:
                                        error = 1
                                        if showing_time [i] == showing:
                                            print(Colour.Red + "TIME OF NEW SHOWING IS REPEATED WITH {}".format(showing_time [i + 1]) + Colour.Reset)
                                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                        else:
                                            print(Colour.Red + "TIME OF NEW SHOWING IS REPEATED WITH {}".format(showing_time [i]) + Colour.Reset)
                                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                    elif start_time [i + 1] <= start_time [i] and end_time [i + 1] > start_time [i] and error == 0:
                                        error = 1
                                        if showing_time [i] == showing:
                                            print(Colour.Red + "TIME OF NEW SHOWING IS REPEATED WITH {}".format(showing_time [i + 1]) + Colour.Reset)
                                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                        else:
                                            print(Colour.Red + "TIME OF NEW SHOWING IS REPEATED WITH {}".format(showing_time [i]) + Colour.Reset)
                                            input(Colour.Yellow + "ENTER TO RETRY" + Colour.Reset)
                                if error == 1:
                                    str_input = ""
                                else:
                                    if not path.exists(path.join(commond_path, 'Showing', showing)):
                                        mkdir(path.join(commond_path, 'Showing', showing))
                                    file_path = path.join(commond_path, 'Showing', showing, 'film.txt')
                                    f = open(file_path, "w")
                                    f.write(filmname + "\n" + dimension + "\n" + language + "\n")
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', showing, 'house.txt')
                                    f = open(file_path, "w")
                                    f.write(house)
                                    f.close()
                                    file_path = path.join(commond_path, 'House', house, 'houseplan.txt')
                                    line = ""
                                    f = open(file_path, "r")
                                    while True:
                                        temp = f.readline()
                                        if temp == "":
                                            break
                                        else:
                                            line += temp
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', showing, 'houseplan.txt')
                                    f = open(file_path, "w")
                                    f.write(line)
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', showing, 'starttime.txt')
                                    f = open(file_path, "w")
                                    f.write(str_input)
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', showing, 'ticket.txt')
                                    f = open(file_path, "w")
                                    f.write("")
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', 'Showing.txt')
                                    f = open(file_path, "a")
                                    f.write(showing + "\n")
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
                                    f = open(file_path, "r")
                                    temp = str(int(f.readline()) + 1)
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
                                    f = open(file_path, "w")
                                    f.write(temp)
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showing.txt')
                                    f = open(file_path, "a")
                                    f.write("upcoming\n" + showing + "\n")
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showingnum.txt')
                                    f = open(file_path, "r")
                                    temp = str(int(f.readline()) + 1)
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', '__Film information', filmname, dimension, language, 'Showingnum.txt')
                                    f = open(file_path, "w")
                                    f.write(temp)
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showing.txt')
                                    f = open(file_path, "a")
                                    f.write("upcoming\n" + showing + "\n")
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showingnum.txt')
                                    f = open(file_path, "r")
                                    temp = str(int(f.readline()) + 1)
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', '__House information', house, 'Showingnum.txt')
                                    f = open(file_path, "w")
                                    f.write(temp)
                                    f.close()
                                    line = ""
                                    for i in range(count_showing_time + 1):
                                        line += datetime.strftime(start_time [i], format_time) + "\n" + timelength_time [i] + "\n" + showing_time [i] + "\n"
                                    file_path = path.join(commond_path, 'Showing', '__House information', house, 'Time.txt')
                                    f = open(file_path, "w")
                                    f.write(line)
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', '__Time information', 'Showing.txt')
                                    f = open(file_path, "a")
                                    f.write("upcoming\n" + showing + "\n")
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt')
                                    f = open(file_path, "r")
                                    temp = str(int(f.readline()) + 1)
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt')
                                    f = open(file_path, "w")
                                    f.write(temp)
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt')
                                    f = open(file_path, "r")
                                    count_showing_time = int(f.readline()) - 1
                                    f.close()
                                    file_path = path.join(commond_path, 'Showing', '__Time information', 'Time.txt')
                                    f = open(file_path, "r")
                                    start_time = []
                                    end_time = []
                                    showing_time = []
                                    timelength_time = []
                                    for i in range(count_showing_time):
                                        line1 = f.readline() [:-1]
                                        line2 = int(f.readline() [:-1])
                                        line3 = f.readline() [:-1]
                                        start_time.append(datetime.strptime(line1, format_time))
                                        timelength_time.append(str(line2))
                                        showing_time.append(line3)
                                    f.close()
                                    start_time.append(start_time_input)
                                    showing_time.append(showing)
                                    timelength_time.append(str(timelength))
                                    for i in range(count_showing_time):
                                        for j in range(count_showing_time):
                                            if start_time [j] > start_time [j + 1]:
                                                temp = start_time [j]
                                                start_time [j] = start_time [j + 1]
                                                start_time [j + 1] = temp
                                                temp = showing_time [j]
                                                showing_time [j] = showing_time [j + 1]
                                                showing_time [j + 1] = temp
                                                temp = timelength_time [j]
                                                timelength_time [j] = timelength_time [j + 1]
                                                timelength_time [j + 1] = temp
                                    f.close()
                                    line = ""
                                    for i in range(count_showing_time + 1):
                                        line += datetime.strftime(start_time [i], format_time) + "\n" + timelength_time [i] + "\n" + showing_time [i] + "\n"
                                    file_path = path.join(commond_path, 'Showing', '__Time information', 'Time.txt')
                                    f = open(file_path, "w")
                                    f.write(line)
                                    f.close()
                                    update_status()
                                    stage = 413
                            else:
                                stage = 401
        #reset system
        elif stage == 501:
            int_input = 0
            verification_code = print_501()
            record = input("")
            if record == verification_code:
                int_input = 1
            if int_input != 0:
                reset_sys()
            stage = 1