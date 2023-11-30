"""print seating plan"""



if __name__ == '__main__':
	input("\033[31mPlease run { __main__.py } in the root directory of this project\033[K")
	quit()


    
from os import path
from .CommondPath import commond_path
from .ClearScreen import clearscreen
from .Colour import Colour
from .CheckDatetime import check_datetime



"""
highlight = -1 for no highlighting
house_or_showing = 0 for showing
                   1 for house
                   3 for ticket
"""
def print_plan(showing: str, housename: str, row_highlight: int, column_highlight: int, house_or_showing: int) -> int:
    if house_or_showing == 0:
        print(Colour.Underline + "Seating plan of {}".format(showing) + Colour.Reset)
        print("")
        file_path = path.join('{}'.format(commond_path), 'Showing', '{}'.format(showing), 'houseplan.txt')
    elif house_or_showing == 1:
        print(Colour.Underline + "Seating plan of {}".format(housename) + Colour.Reset)
        print("")
        file_path = path.join('{}'.format(commond_path), 'House', '{}'.format(housename), 'houseplan.txt')
    else:
        print(Colour.Underline + "T" + showing [1:] + int_to_eng(row_highlight) + str(column_highlight) + Colour.Reset)
        print("")
        file_path = path.join('{}'.format(commond_path), 'Showing', '{}'.format(showing), 'houseplan.txt')
    f = open(file_path, "r")
    seating_plan = []
    avail_seat = 0
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
    row_len = len(str(row))
    column_len = len(str(column))
    print("{:^{}}".format("COLUMN", (row_len + 2) * 2 + (column_len + 2) * column + 1))
    print("")
    print(end = " ")
    for i in range(row_len + 1):
        print(end = " ")
    for i in range(1, column + 1):
        print("{:^{}}".format(i, column_len + 2), end = "")
    print("")
    R_print = row
    O_print = row + 1
    W_print = row + 2
    x = 0
    for i in range(row - 1, -1, -1):
        for j in range(row_len + 2):
            print(end = " ")
        for j in range((column_len + 2) * column + 1):
            print("-", end = "")
        x += 1
        if x == R_print:
            for j in range(row_len + 3):
                print(end = " ")
            print(end = "R")
        elif x == O_print:
            for j in range(row_len + 3):
                print(end = " ")
            print(end = "O")
        elif x == W_print:
            for j in range(row_len + 3):
                print(end = " ")
            print(end = "W")
        print("")
        print("{:>{}}".format(int_to_eng(i), row_len + 1), end = " ")
        for j in range(column):
            print("|", end = "")
            if i == row_highlight and j == column_highlight:
                print(Colour.Highlight, end = "")
            if seating_plan [i][j] == "0":
                avail_seat += 1
                print(Colour.Green + "{:^{}}".format("O", column_len + 1) + Colour.Reset, end = "")
            elif seating_plan [i][j] == "1":
                print(Colour.Red + "{:^{}}".format("X", column_len + 1) + Colour.Reset, end = "")
            else:
                print(Colour.Blue + "{:^{}}".format("\ua554", column_len + 1) + Colour.Reset, end = "")
        print("|", end = " ")
        print("{:<{}}".format(int_to_eng(i), row_len + 1), end = " ")
        x += 1
        if x == R_print:
            print(end = "R")
        elif x == O_print:
            print(end = "O")
        elif x == W_print:
            print(end = "W")
        print("")
    for i in range(row_len + 2):
        print(end = " ")
    for i in range((column_len + 2) * column + 1):
        print("-", end = "")
    if row == 1:
        for i in range(row_len + 3):
            print(end = " ")
        print(end = "W")
    print("")
    print("")
    print("{}{:^{}}{}".format(Colour.BWhite, "SCREEN", (row_len + 2) * 2 + (column_len + 2) * column + 1, Colour.Reset))
    print("")
    return avail_seat



def int_to_eng(a) -> str:
    bigrow = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    strrow = ""
    x = 0
    if a > 25:
        while x == 0:
            b = int(a / 26)
            c = a % 26
            if b > 26:
                strrow = bigrow[c] + strrow
                a = b - 1
            else:
                strrow = bigrow[c] + strrow
                strrow = bigrow[b - 1] + strrow
                x = 1
    else:
        strrow = bigrow[a] + strrow
    return strrow