"""
Stage     Output

0     --> Log out
1     --> Film (include Filmname Rating Timelength)
2     --> Film (include Dimension Language Price Rating Timelength)
3     --> Showings (include Dimension Language Price Rating Timelength Starttime Endtime available/allseat)
4     --> Seatingplan
"""



from os import path
from time import sleep
from datetime import datetime, timedelta
from .CommondPath import commond_path
from .ClearScreen import clearscreen
from .Colour import Colour
from .CheckDatetime import check_datetime
from .Seatingplan import print_plan
from .UpdateDatetimeAll import update_status



def input_int_check(output: str, choose) -> int:
    str_input: str = input(output)
    if str_input.isdecimal() and int(str_input) != 0 and int(str_input) <= choose:
        return int(str_input)
    else:
        print(Colour.Reset + Colour.Red + "YOUR INPUT IS INCORRECT" + Colour.Reset)
        input(Colour.Reset + Colour.Yellow + "PRESS ENTER TO RETRY" + Colour.Reset)
        return 0



def stage1_print() -> int:
    print(Colour.Underline + "Film" + Colour.Reset)
    print("")
    film_name = []
    file_path = path.join('{}'.format(commond_path), 'Film', 'filmname.txt')
    f = open(file_path, "r")
    count_film: str = int(f.readline() [:-1])
    len_count_film: str = len(str(count_film))
    for i in range(count_film):
        film_name.append(str(f.readline() [:-1]))
    f.close()
    film_len = 0
    for i in range(count_film):
        if film_len < len(film_name [i]):
            film_len = len(film_name [i])
    film_rating = []
    for i in range(count_film):
        file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film_name [i]), 'rating.txt')
        f = open(file_path, "r")
        film_rating.append(str(f.readline()))
        f.close()
    film_timelength = []
    for i in range(count_film):
        file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film_name [i]), 'timelength.txt')
        f = open(file_path, "r")
        film_timelength.append(str(f.readline()))
        f.close()
    for i in range(count_film):
        print("{:<{}}   -->   {:<{}}   {:<{}}   {} minutes".format(i + 1, len_count_film, film_name [i], film_len, film_rating [i], 3, film_timelength [i]))
    print("{:<{}}   -->   Log out".format(i + 2, len_count_film))
    print("")
    return i + 2



def stage2_print(film) -> int:
    file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film), 'rating.txt')
    f = open(file_path, "r")
    rating = f.readline()
    f.close()
    file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film), 'timelength.txt')
    f = open(file_path, "r")
    timelength = f.readline()
    f.close()
    file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film), 'dimension.txt')
    dimension = []
    f = open(file_path, "r")
    count_dimension = int(f.readline())
    for i in range(count_dimension):
        dimension.append(f.readline() [:-1])
    f.close()
    file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film), 'language.txt')
    language = []
    f = open(file_path, "r")
    count_language = int(f.readline())
    for i in range(count_language):
        language.append(f.readline() [:-1])
    f.close()
    price = []
    file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film), 'price.txt')
    f = open(file_path, "r")
    for i in range(count_dimension):
        price.append(f.readline() [:-1])
    f.close()
    st_price = []
    file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film), 'st_price.txt')
    f = open(file_path, "r")
    for i in range(count_dimension):
        st_price.append(f.readline() [:-1])
    f.close()
    len_count = len(str(count_dimension * count_language))
    len_language = 0
    for i in range(count_language):
        if len_language < len(language [i]):
            len_language = len(language [i])
    len_dimension = 0
    for i in range(count_dimension):
        if len_dimension < len(dimension [i]):
            len_dimension = len(dimension [i])
    print(Colour.Underline + "{}   {}   {} minutes".format(film, rating, timelength) + Colour.Reset)
    print("")
    for i in range(count_dimension):
        for j in range(count_language):
            print("{:<{}}   -->   {:<{}}   {:<{}}   Adult   price: $ {}".format((i + 1) * (j + 1), len_count, dimension [i], len_dimension, language [j], len_language, price [i]))
            print("{}         {}   {}   Student price: $ {}".format(" " * len_count, " " * len_dimension, " " * len_language, st_price [i]))
    print("{:<{}}   -->   Go back".format((i + 1) * (j + 1) + 1, len_count))
    print("")
    return (i + 1) * (j + 1) + 1



def stage3_print(sub_film_name: str, sub_dimension: str, sub_language: str, sub_time_length: int, sub_price: int, sub_rating: str) -> int:
    print(Colour.Underline + "Upcoming Showings of {} {} {}".format(sub_film_name, sub_dimension, sub_language) + Colour.Reset)
    print("")
    if not path.exists(path.join(commond_path, 'Showing', '__Film information', sub_film_name, sub_dimension, sub_language, 'Showing.txt')):
        print("There is no showing matching condition.")
        print("1 <-- Go back")
        print("")
        return 1
    else:
        file_path = path.join('{}'.format(commond_path), 'Showing', '__Film information', '{}'.format(sub_film_name), '{}'.format(sub_dimension), '{}'.format(sub_language), 'Showingnum.txt')
        f = open(file_path)
        x: int = int(f.readline())
        showing_num = 0
        f.close()
        file_path = path.join('{}'.format(commond_path), 'Showing', '__Film information', '{}'.format(sub_film_name), '{}'.format(sub_dimension), '{}'.format(sub_language), 'Showing.txt')
        showing = []
        f = open(file_path)
        for i in range(x):
            if f.readline() [:-1] == "upcoming":
                showing.append(f.readline() [:-1])
                showing_num += 1
            else:
                f.readline()
        f.close()
        len_showing_num = len(str(showing_num + 1))
        format_time = "%d/%m/%y %H:%M:%S"
        temp = []
        for i in range(showing_num):
            file_path = path.join('{}'.format(commond_path), 'Showing', '{}'.format(showing [i]), 'starttime.txt')
            f = open(file_path)
            temp.append(f.readline())
            f.close()
        start_time = []
        for i in temp:
            start_time.append(datetime.strptime(i, format_time))
        end_time = []
        for i in range(showing_num):
            end_time.append(start_time [i] + timedelta(minutes = sub_time_length))
        house = []
        for i in range(showing_num):
            file_path = path.join('{}'.format(commond_path), 'Showing', '{}'.format(showing [i]), 'house.txt')
            f = open(file_path)
            house.append(f.readline())
            f.close()
        avail_seat = []
        all_seat = []
        for i in range(showing_num):
            file_path = path.join('{}'.format(commond_path), 'Showing', '{}'.format(showing [i]), 'houseplan.txt')
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
            avail_seat.append(avail_count)
            all_seat.append(column * row)
            f.close()
        i = 0
        count = 0
        for i in range(1, showing_num + 1):
            if start_time [i - 1] <= datetime.now() + timedelta(days = 7):
                count += 1
                print("{:<{}} --> {}{}{}".format(count, len_showing_num, Colour.Underline, showing [i - 1], Colour.Reset))
                print("{:<{}}     Time : {} - {}".format(" ", len_showing_num, str(start_time [i - 1]), str(end_time [i - 1])))
                print("{:<{}}     House: {}".format(" ", len_showing_num, house [i - 1]))
                if avail_seat [i - 1] == 0:
                    haha = Colour.Red
                elif avail_seat [i - 1] / all_seat [i - 1] <= 0.5:
                    haha = Colour.Yellow
                else:
                    haha = Colour.Green
                print("{:<{}}     Seat : {}{}{}/{}".format(" ", len_showing_num, haha, avail_seat [i - 1], Colour.Reset, all_seat [i - 1]))
        print("{:<{}} --> Go back".format(count + 1, len_showing_num))
        print("")
        return count + 1



def stage4_print(sub_showing, price, st_price):
    seat_count = print_plan(sub_showing, "", -1, -1, 0)
    print(Colour.Underline + "Status of seats" + Colour.Reset + ":")
    print(Colour.Green + "O" + Colour.Reset + " <-> Available seats")
    print(Colour.Red + "X" + Colour.Reset + " <-> Sold seats")
    print(Colour.Blue + "\ua554" + Colour.Reset + " <-> Unavailable seats")
    print("")
    print("Adult   price: $ " + price)
    print("Student price: $ " + st_price)
    print("")
    print("Input \"exit\" --> exit")
    print("")
    return seat_count



def stage5_print(showing, list_ticket, price, st_price, count_ticket, count_student):
    seat_count = print_plan(showing, "", -1, -1, 0)
    print(Colour.Underline + "Status of seats" + Colour.Reset + ":")
    print(Colour.Green + "O" + Colour.Reset + " <-> Available seats")
    print(Colour.Red + "X" + Colour.Reset + " <-> Sold seats")
    print(Colour.Blue + "\ua554" + Colour.Reset + " <-> Unavailable seats")
    print("")
    print(Colour.Underline + "Ticket information" + Colour.Reset)
    len_list_ticket = 0
    for i in list_ticket:
        if len_list_ticket < len(i):
            len_list_ticket = len(i)
    total_price = int(price) * (count_ticket - count_student) + int(st_price) * count_student
    len_total_price = len(str(total_price))
    print(" " * (len_list_ticket + 18 + len_total_price) + "$")
    for i in list_ticket:
        if i [len(i) - 1] == "A":
            print("{:<{}}    Adult  price   {:>{}}".format(i, len_list_ticket, price, len_total_price))
        else:
            print("{:<{}}   Student price   {:>{}}".format(i, len_list_ticket, st_price, len_total_price))
    print("-" * (len_list_ticket + 19 + len_total_price))
    print(" " * (len_list_ticket + 19) + Colour.Underline + str(total_price) + Colour.Reset)
    print(" " * (len_list_ticket + 19) + Colour.Underline + " " * len_total_price + Colour.Reset)
    print(Colour.Green + "BUYING SUCCESSING" + Colour.Reset)
    input(Colour.Yellow + "ENTER TO GO BACK TO THE MENU" + Colour.Reset)




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



def user_version():
    stage = 1
    while stage != 0:
        clearscreen()
        if stage == 1:
            int_input = 0
            while int_input == 0:
                choose = stage1_print()
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input < choose:
                file_path = path.join('{}'.format(commond_path), 'Film', 'filmname.txt')
                f = open(file_path, "r")
                for i in range(int_input):
                    f.readline()
                film_name: str = f.readline() [:-1]
                f.close()
                stage = 2
            elif int_input == choose:
                stage = 0
        elif stage == 2:
            int_input = 0
            while int_input == 0:
                choose = stage2_print(film_name)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input < choose:
                file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film_name), 'language.txt')
                f = open(file_path, "r")
                count_language = int(f.readline())
                f.close()
                count_dimension = 1
                while int_input > count_language:
                    int_input -= count_language
                    count_dimension += 1
                file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film_name), 'dimension.txt')
                f = open(file_path, "r")
                for i in range(count_dimension):
                    f.readline()
                dimension: str = f.readline() [:-1]
                f.close()
                file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film_name), 'language.txt')
                f = open(file_path, "r")
                for i in range(int_input):
                    f.readline()
                language: str = f.readline() [:-1]
                file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film_name), 'price.txt')
                f = open(file_path, "r")
                for i in range(count_dimension - 1):
                    f.readline()
                price: int = int(f.readline() [:-1])
                file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film_name), 'rating.txt')
                f = open(file_path)
                rating: str = f.readline()
                f.close()
                file_path = path.join('{}'.format(commond_path), 'Film', '{}'.format(film_name), 'timelength.txt')
                f = open(file_path)
                time_length: int = int(f.readline())
                f.close()
                update_status()
                stage = 3
            elif int_input == choose:
                stage = 1
        elif stage == 3:
            int_input = 0
            while int_input == 0:
                choose = stage3_print(film_name, dimension, language, time_length, price, rating)
                int_input = input_int_check("Input number: ", choose)
                clearscreen()
            if int_input < choose:
                file_path = path.join('{}'.format(commond_path), 'Showing', '__Film information', '{}'.format(film_name), '{}'.format(dimension), '{}'.format(language), 'Showingnum.txt')
                f = open(file_path)
                x: int = int(f.readline())
                showing_num = 0
                f.close()
                file_path = path.join('{}'.format(commond_path), 'Showing', '__Film information', '{}'.format(film_name), '{}'.format(dimension), '{}'.format(language), 'Showing.txt')
                showingx = []
                f = open(file_path)
                for i in range(x):
                    if f.readline() [:-1] == "upcoming":
                        showingx.append(f.readline() [:-1])
                        showing_num += 1
                    else:
                        f.readline()
                f.close()
                showing = showingx [int_input - 1]
                format_time = "%d/%m/%y %H:%M:%S"
                file_path = path.join('{}'.format(commond_path), 'Showing', '{}'.format(showing), 'starttime.txt')
                f = open(file_path, "r")
                start_time:datetime = datetime.strptime(f.readline(), format_time)
                f.close()
                end_time:datetime = start_time + timedelta(minutes = time_length)
                if check_datetime(showing) == 2:
                    print("")
                    print(Colour.Red + "THIS SHOWING [{}] HAD ENDED".format(showing) + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO COUNTINUE" + Colour.Reset)
                    clearscreen()
                    stage = 1
                elif check_datetime(showing) == 1:
                    print("")
                    print(Colour.Red + "THIS SHOWING [{}] HAS STARTED".format(showing) + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO COUNTINUE" + Colour.Reset)
                    clearscreen()
                    stage = 1
                else:
                    stage = 4
            elif int_input == choose:
                stage = 2
        elif stage == 4:
            file_path = path.join(commond_path, 'Film', film_name, 'price.txt')
            f = open(file_path, "r")
            for i in range(count_dimension - 1):
                f.readline()
            price = f.readline() [:-1]
            f.close()
            file_path = path.join(commond_path, 'Film', film_name, 'st_price.txt')
            f = open(file_path, "r")
            for i in range(count_dimension - 1):
                f.readline()
            st_price = f.readline() [:-1]
            while True:
                exit_input = 0
                choose = stage4_print(showing, price, st_price)
                str_input = input("Input coordinates of seats e.g.(A1 A2 A3): ")
                record_input = str_input
                if str_input == "exit" or str_input == "Exit" or str_input == "EXIT":
                    exit_input = 1
                    break
                elif check_datetime(showing) == 2:
                    exit_input = 1
                    print("")
                    print(Colour.Red + "THIS SHOWING [{}] HAD ENDED".format(showing) + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO COUNTINUE" + Colour.Reset)
                    break
                elif check_datetime(showing) == 1:
                    exit_input = 1
                    print("")
                    print(Colour.Red + "THIS SHOWING [{}] HAS STARTED".format(showing) + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO COUNTINUE" + Colour.Reset)
                    break
                while str_input != "" and str_input [0] == " ":
                    str_input = str_input [1:]
                while str_input != "" and str_input [len(str_input) - 1] == " ":
                    str_input = str_input [:-1]
                str_input += " "
                list_ticket = []
                temp = ""
                for i in range(len(str_input)):
                    if str_input [i] == " ":
                        if temp != "":
                            list_ticket.append(temp.upper())
                            temp = ""
                    else:
                        temp += str_input [i]
                if str_input != " ":
                    error = 0
                    row_ticket = []
                    column_ticket = []
                    count_ticket = 0
                    for i in list_ticket:
                        count_ticket += 1
                        if error == 0:
                            if i [0].isalpha():
                                j = i + " "
                                temp = ""
                                while j [0].isalpha():
                                    temp += j [0]
                                    j = j [1:]
                                row_ticket.append(temp)
                                temp = ""
                                while j [0].isdigit():
                                    temp += j [0]
                                    j = j [1:]
                                column_ticket.append(temp)
                                if j != " " or temp == "":
                                    error = 1
                            elif i [0].isdigit():
                                j = i + " "
                                temp = ""
                                while j [0].isdigit():
                                    temp += j [0]
                                    j = j [1:]
                                column_ticket.append(temp)
                                temp = ""
                                while j [0].isalpha():
                                    temp += j [0]
                                    j = j [1:]
                                row_ticket.append(temp)
                                if j != " " or temp == "":
                                    error = 1
                            else:
                                error = 1
                    for i in range(count_ticket):
                        for j in range(i + 1, count_ticket):
                            if list_ticket [i] == list_ticket [j]:
                                error = 1
                    if error == 0:
                        file_path = path.join(commond_path, 'Showing', showing, 'houseplan.txt')
                        f = open(file_path, "r")
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
                        error = 0
                        for i in range(count_ticket):
                            if int(column_ticket [i]) == 0:
                                error = 1
                        if error == 0:
                            try:
                                list_unavailable = []
                                for i in range(count_ticket):
                                    if seating_plan [eng_to_int(row_ticket [i])][int(column_ticket [i]) - 1] != "0":
                                        error = 1
                                        list_unavailable.append(row_ticket [i].upper() + column_ticket [i])
                                if error == 1:
                                    print(Colour.Red)
                                    print("SEAT [ " + list_unavailable [0], end = "")
                                    del list_unavailable [0]
                                    for i in list_unavailable:
                                        print(", " + i, end = "")
                                    print(" ] IS UNAVAILABLE" + Colour.Reset)
                                    input(Colour.Yellow + "ENTER TO COUNTINUE" + Colour.Reset)
                                else:
                                    break
                            except IndexError:
                                print("")
                                print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                                input(Colour.Yellow + "ENTER TO COUNTINUE" + Colour.Reset)
                        else:
                            print("")
                            print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                            input(Colour.Yellow + "ENTER TO COUNTINUE" + Colour.Reset)
                    else:
                        print("")
                        print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                        input(Colour.Yellow + "ENTER TO COUNTINUE" + Colour.Reset)
                else:
                    print("")
                    print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO COUNTINUE" + Colour.Reset)
            while exit_input == 0:
                clearscreen()
                choose = stage4_print(showing, price, st_price)
                print("Input coordinates of seats e.g.(A1 A2 A3): " + record_input)
                print("")
                str_input = input("Input numbers of children and students: ")
                if str_input == "exit" or str_input == "Exit" or str_input == "EXIT":
                    exit_input = 1
                    break
                elif check_datetime(showing) == 2:
                    exit_input = 1
                    print("")
                    print(Colour.Red + "THIS SHOWING [{}] HAD ENDED".format(showing) + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO COUNTINUE" + Colour.Reset)
                    clearscreen()
                    break
                elif check_datetime(showing) == 1:
                    exit_input = 1
                    print("")
                    print(Colour.Red + "THIS SHOWING [{}] HAS STARTED".format(showing) + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO COUNTINUE" + Colour.Reset)
                    clearscreen()
                    break
                while str_input != "" and str_input [0] == " ":
                    str_input = str_input [1:]
                while str_input != "" and str_input [len(str_input) - 1] == " ":
                    str_input = str_input [:-1]
                if str_input.isdecimal() and int(str_input) <= count_ticket:
                    count_students = int(str_input)
                    break
                else:
                    print("")
                    print(Colour.Red + "INPUT INCORRECT" + Colour.Reset)
                    input(Colour.Yellow + "ENTER TO COUNTINUE" + Colour.Reset)
            if exit_input == 0:
                for i in range(count_ticket):
                    seating_plan [eng_to_int(row_ticket [i])][int(column_ticket [i]) - 1] = "1"
                file_path = path.join(commond_path, 'Showing', showing, 'houseplan.txt')
                f = open(file_path, "w")
                line = ""
                for i in range(row):
                    for j in range(column):
                        line += seating_plan [i][j]
                    line += "\n"
                f.write(line)
                f.close()
                file_path = path.join(commond_path, 'Showing', showing, 'ticket.txt')
                f = open(file_path, "r")
                count_list_ticket = 0
                row_list_ticket = []
                column_list_ticket = []
                st_list_ticket = []
                while True:
                    line = f.readline()
                    if line == "":
                        break
                    else:
                        count_list_ticket += 1
                        line = line [11:-1]
                        temp = ""
                        while line [0].isalpha():
                            temp += line [0]
                            line = line [1:]
                        row_list_ticket.append(temp)
                        temp = ""
                        while line [0].isdigit():
                            temp += line [0]
                            line = line [1:]
                        column_list_ticket.append(temp)
                        st_list_ticket.append(line)
                f.close()
                for i in range(count_ticket):
                    count_list_ticket += 1
                    row_list_ticket.append(row_ticket [i].upper())
                    column_list_ticket.append(column_ticket [i])
                for i in range(count_students):
                    st_list_ticket.append("S")
                for i in range(count_ticket - count_students):
                    st_list_ticket.append("A")
                for i in range(count_list_ticket):
                    for j in range(count_list_ticket - 1):
                        if eng_to_int(row_list_ticket [j]) > eng_to_int(row_list_ticket [j + 1]):
                            temp = row_list_ticket [j]
                            row_list_ticket [j] = row_list_ticket [j + 1]
                            row_list_ticket [j + 1] = temp
                            temp = column_list_ticket [j]
                            column_list_ticket [j] = column_list_ticket [j + 1]
                            column_list_ticket [j + 1] = temp
                            temp = st_list_ticket [j]
                            st_list_ticket [j] = st_list_ticket [j + 1]
                            st_list_ticket [j + 1] = temp
                        elif eng_to_int(row_list_ticket [j]) == eng_to_int(row_list_ticket [j + 1]):
                            if int(column_list_ticket [j]) > int(column_list_ticket [j + 1]):
                                temp = row_list_ticket [j]
                                row_list_ticket [j] = row_list_ticket [j + 1]
                                row_list_ticket [j + 1] = temp
                                temp = column_list_ticket [j]
                                column_list_ticket [j] = column_list_ticket [j + 1]
                                column_list_ticket [j + 1] = temp
                                temp = st_list_ticket [j]
                                st_list_ticket [j] = st_list_ticket [j + 1]
                                st_list_ticket [j + 1] = temp
                line = ""
                for i in range(count_list_ticket):
                    line += "T" + showing [1:] + row_list_ticket [i] + column_list_ticket [i] + st_list_ticket [i] + "\n"
                f = open(file_path, "w")
                f.write(line)
                f.close()
                stage = 5
            else:
                stage = 3
        elif stage == 5:
            list_ticket = []
            for i in range(count_ticket):
                if i < count_students:
                    list_ticket.append("T" + showing [1:] + row_ticket [i].upper() + column_ticket [i] + "S")
                else:
                    list_ticket.append("T" + showing [1:] + row_ticket [i].upper() + column_ticket [i] + "A")
            stage5_print(showing, list_ticket, price, st_price, count_ticket, count_students)
            stage = 1
    clearscreen()
    list_logout = ["\\", "|", "/", "-"]
    for i in range(3):
        for j in list_logout:
            print("\rLoging out in {} seconds {}".format(3 - i, j), end = "")
            sleep(0.25)
    clearscreen()
    return
