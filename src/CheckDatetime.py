"""check and update the status of Showing (one) (previous, playing, upcoming)"""



from os import path
from datetime import datetime, timedelta
from .UpdateDatetime import update_status_film_inf, update_status_time_inf, update_status_house_inf
from .CommondPath import commond_path
from .ClearScreen import clearscreen
from .Colour import Colour



def check_datetime(sub_showing) -> int:
    format_time = "%d/%m/%y %H:%M:%S"
    time_now = datetime.strftime(datetime.now(), format_time)
    time_now = datetime.strptime(time_now, format_time)
    file_path = path.join('{}'.format(commond_path), 'Showing', '{}'.format(sub_showing), 'film.txt')
    f = open(file_path, "r")
    film = f.readline() [:-1]
    f.close()
    file_path = path.join(commond_path, 'Film', film, 'timelength.txt')
    f = open(file_path, "r")
    time_length = int(f.readline())
    f.close()
    file_path = path.join(commond_path, 'Showing', sub_showing, 'starttime.txt')
    f = open(file_path, "r")
    sub_start_time:datetime = datetime.strptime(f.readline(), format_time)
    f.close()
    sub_end_time:datetime = sub_start_time + timedelta(minutes = time_length)
    if time_now >= sub_end_time:
        update_status_film_inf(sub_showing, "previous")
        update_status_time_inf(sub_showing, "previous")
        update_status_house_inf(sub_showing, "previous")
        return 2
    elif time_now >= sub_start_time:
        update_status_film_inf(sub_showing, "playing")
        update_status_time_inf(sub_showing, "playing")
        update_status_house_inf(sub_showing, "playing")
        return 1
    else:
        update_status_film_inf(sub_showing, "upcoming")
        update_status_time_inf(sub_showing, "upcoming")
        update_status_house_inf(sub_showing, "upcoming")
        return 0