"""According filmname.txt and housename.txt and language.txt"""



from os import path
from .CommondPath import commond_path



def eng_to_int(strinput: str) -> int:
    bigrow = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    smallrow = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    i = len(strinput)
    num = 0
    while i > 0 and strinput != "":
        error = 1
        for j in range(0, 26):
            if strinput [i - 1] == smallrow [j] or strinput [i - 1] == bigrow [j]:
                num += j * (26 ** (i - 1))
                error = 0
                j = 26
        if error == 1:
            i = -1
        else:
            i -= 1
    if i == 0 and strinput != "":
        return num
    else:
        return -1
    


def housename_accord():
    file_path = path.join(commond_path, 'House', 'housename.txt')
    f = open(file_path, "r")
    count_house = int(f.readline() [:-1])
    list_house = []
    for i in range(count_house):
        list_house.append(f.readline() [:-1])
    f.close()
    list_house.sort(key = lambda v: v.lower())
    line = str(count_house) + "\n"
    for i in range(count_house):
        line += list_house [i] + "\n"
    f = open(file_path, "w")
    f.write(line)
    f.close()



def filmname_accord():
    file_path = path.join(commond_path, 'Film', 'filmname.txt')
    f = open(file_path, "r")
    count_film = int(f.readline() [:-1])
    list_film = []
    for i in range(count_film):
        list_film.append(f.readline() [:-1])
    f.close()
    list_film.sort(key = lambda v: v.lower())
    line = str(count_film) + "\n"
    for i in range(count_film):
        line += list_film [i] + "\n"
    f = open(file_path, "w")
    f.write(line)
    f.close()



def ticket_accord():
    g = open(path.join(commond_path, 'Showing', 'Showing.txt'))
    while True:
        showing = g.readline() [:-1]
        if showing == "":
            break
        else:
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