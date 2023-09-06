"""
Showing.self
       .starttime
       .endtime
       
       .house
       .seatingplan
       
       .film
       .dimension
       .language
       .price
       .rating
       .timelength
"""



from pathlib import Path
from os import path
from datetime import datetime



class Showingalldata:

    def __init__(self):
        pass

    def setStartTime(self, starttime):
        self.starttime = starttime

    def setHouse(self, housename: str):
        is_exist = path.exists(Path("Data/House/{}".format(housename)))
        if is_exist:
            self.house = housename
            
            dir_path = Path("Data", "House", "{}".format(housename))

            file_name = "row.txt"
            file_path = dir_path.joinpath(file_name)
            f = open(file_path, "r")
            row = int(f.readline())
            f.close()

            file_name = "column.txt"
            file_path = dir_path.joinpath(file_name)
            f = open(file_path, "r")
            column = int(f.readline())
            f.close()

            self.seatingplan = []
            for i in range(row):
                temp = []
                for j in range(column):
                    temp.append(0)
                self.seatingplan.append(temp)

    def setFilm(self, film: str, dimension: str):
        self.endtime
        self.film
        self.dimension
        self.language
        self.price
        self.rating
        self.timelength
