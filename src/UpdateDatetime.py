"""update the status of Showings (one)(previous, playing, upcoming)"""



from os import path
from datetime import datetime
from .CommondPath import commond_path



"""ONE"""
def update_status_film_inf(showing, current_status: str) -> None:
    file_path = path.join('{}'.format(commond_path), 'Showing', '{}'.format(showing), 'film.txt')
    f = open(file_path, "r")
    film = f.readline() [:-1]
    dimension = f.readline() [:-1]
    language = f.readline() [:-1]
    f.close()
    file_path = path.join('{}'.format(commond_path), 'Showing', '__Film information', '{}'.format(film), '{}'.format(dimension), '{}'.format(language), 'Showingnum.txt')
    f = open(file_path, "r")
    count = int(f.readline())
    f.close()
    line = []
    file_path = path.join('{}'.format(commond_path), 'Showing', '__Film information', '{}'.format(film), '{}'.format(dimension), '{}'.format(language), 'Showing.txt')
    f = open(file_path)
    for i in range(count * 2):
        line.append(str(f.readline()))
    f.close()
    f = open(file_path, "w")
    f.write("")
    f.close()
    f = open(file_path, "a")
    for i in range(0, count * 2, 2):
        if line [i + 1] == showing + "\n":
            string_write = current_status + "\n"
            f.write(string_write)
            string_write = showing + "\n"
            f.write(string_write)
        else:
            string_write = line [i]
            f.write(string_write)
            string_write = line [i + 1]
            f.write(string_write)
    f.close()



"""ONE"""
def update_status_time_inf(showing, current_status: str) -> None:
    file_path = path.join('{}'.format(commond_path), 'Showing', '__Time information', 'Showingnum.txt')
    f = open(file_path, "r")
    count = int(f.readline())
    f.close()
    file_path = path.join('{}'.format(commond_path), 'Showing', '__Time information', 'Showing.txt')
    line = []
    f = open(file_path)
    for i in range(count * 2):
        line.append(str(f.readline()))
    f.close()
    f = open(file_path, "w")
    f.write("")
    f.close()
    f = open(file_path, "a")
    for i in range(0, count * 2, 2):
        if line [i + 1] == showing + "\n":
            string_write = current_status + "\n"
            f.write(string_write)
            string_write = showing + "\n"
            f.write(string_write)
        else:
            string_write = line [i]
            f.write(string_write)
            string_write = line [i + 1]
            f.write(string_write)
    f.close()



"""ONE"""
def update_status_house_inf(showing, current_status: str) -> None:
    file_path = path.join('{}'.format(commond_path), 'Showing', '{}'.format(showing), 'house.txt')
    f = open(file_path, "r")
    house = f.readline()
    f.close()
    file_path = path.join('{}'.format(commond_path), 'Showing', '__House information', '{}'.format(house), 'Showingnum.txt')
    f = open(file_path)
    count = int(f.readline())
    f.close()
    file_path = path.join('{}'.format(commond_path), 'Showing', '__House information', '{}'.format(house), 'Showing.txt')
    line = []
    f = open(file_path)
    for i in range(count * 2):
        line.append(str(f.readline()))
    f.close()
    f = open(file_path, "w")
    f.write("")
    f.close()
    f = open(file_path, "a")
    for i in range(0, count * 2, 2):
        if line [i + 1] == showing + "\n":
            string_write = current_status + "\n"
            f.write(string_write)
            string_write = showing + "\n"
            f.write(string_write)
        else:
            string_write = line [i]
            f.write(string_write)
            string_write = line [i + 1]
            f.write(string_write)
    f.close()
