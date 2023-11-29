"""if file not exist, create it"""



from os import path, mkdir, walk
from .CommondPath import commond_path



def file_data():
    file_missing = 0
    file_path = path.join(commond_path, 'Data')
    if not path.exists(file_path):
        file_missing = 1
    if file_missing == 0:
        file_missing = file_account()
    if file_missing == 0:
        file_missing = file_house()
    if file_missing == 0:
        file_missing = file_film()
    if file_missing == 0:
        file_missing = file_showing()
    if file_missing == 1:
        ...



def file_account():
    file_path = path.join(commond_path, 'Account')
    if not path.exists(file_path):
        return 1
    file_path = path.join(commond_path, 'Account', 'admin.txt')
    if not path.exists(file_path):
        return 1
    file_path = path.join(commond_path, 'Account', 'user.txt')
    if not path.exists(file_path):
        return 1
    file_path = path.join(commond_path, 'Account', 'admin_login_time.txt')
    if not path.exists(file_path):
        return 1
    file_path = path.join(commond_path, 'Account', 'user_login_time.txt')
    if not path.exists(file_path):
        return 1



def file_house():
    file_path = path.join(commond_path, 'House')
    if not path.exists(file_path):
        return 1
    file_path = path.join(commond_path, 'House', 'housename.txt')
    if not path.exists(file_path):
        return 1
    else:
        f = open(file_path, "r")
        count_house = int(f.readline() [:-1])
        list_file = ["allseat.txt", "houseplan.txt"]
        for i in range(count_house):
            for j in list_file:
                if not path.exists(path.join(commond_path, 'Data', 'House', f.readline() [:-1], j)):
                    return 1



def file_film():
    file_path = path.join(commond_path, 'Film')
    if not path.exists(file_path):
        return 1
    file_path = path.join(commond_path, 'Film', 'filmname.txt')
    if not path.exists(file_path):
        return 1
    else:
        f = open(file_path, "r")
        count_film = int(f.readline() [:-1])
        list_file = ["dimension.txt", "language.txt", "price.txt", "rating.txt", "st_price.txt", "timelength.txt"]
        for i in range(count_film):
            for j in list_file:
                if not path.exists(path.join(commond_path, 'Data', 'House', f.readline() [:-1], j)):
                    return 1



def file_showing():
    file_path = path.join(commond_path, 'Showing')
    if not path.exists(file_path):
        return 1
    file_path = path.join(commond_path, 'Showing', 'Missshowing.txt')
    if not path.exists(file_path):
        return 1
    file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
    if not path.exists(file_path):
        return 1
    else:
        f = open(file_path, "r")
        count_showing = int(f.readline())
        f.close()
        file_path = path.join(commond_path, 'Showing', 'Showing.txt')
        if not path.exists(file_path):
            return 1
        else:
            f = open(file_path, "r")
            list_file = ['film.txt', 'house.txt', 'houseplan.txt', 'starttime.txt', 'ticket.txt']
            for i in range(count_showing):
                for j in list_file:
                    if not path.exists(path.join(commond_path, 'Data', 'Showing', f.readline() [:-1], j)):
                        return 1
    file_path = path.join(commond_path, 'Showing', '__Time information')
    if not path.exists(file_path):
        return 1
    file_path = path.join(commond_path, 'Showing', '__Time information', 'Showing.txt')
    if not path.exists(file_path):
        return 1
    file_path = path.join(commond_path, 'Showing', '__Time information', 'Showingnum.txt')
    if not path.exists(file_path):
        return 1
    file_path = path.join(commond_path, 'Showing', '__Time information', 'Time.txt')
    if not path.exists(file_path):
        return 1
    file_path = path.join(commond_path, 'Showing', '__Time information')
    file_path = path.join(commond_path, 'House', 'housename.txt')