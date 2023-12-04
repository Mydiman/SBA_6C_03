
"""update the status of all Showings (previous, playing, upcoming)"""



if __name__ == '__main__':
	input("\033[31mPlease run { __main__.py } in the root directory of this project\033[K")
	quit()
     

     
from os import path
from datetime import datetime
from time import sleep
from .CommondPath import commond_path
from .ClearScreen import clearscreen
from .CheckDatetime import check_datetime



def update_status():
    clearscreen()
    print("Please wait for a while.")
    file_path = path.join(commond_path, 'Showing', 'Showingnum.txt')
    f = open(file_path, "r")
    count = int(f.readline())
    f.close()
    file_path = path.join(commond_path, 'Showing', 'Showing.txt')
    f = open(file_path)
    for i in range(count):
        check_datetime(f.readline()[:-1])
    f.close()
    clearscreen()