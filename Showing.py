"""
Showing.self         __init__(self)

       .starttime    setStartTime(self, starttime)
       
       .house        setHouse(self, housename: str)
       .seatingplan
       
       .film         setFilm(self, film: str, dimension: str)
       .dimension
       .language
       .price
       .rating
       .timelength
       .endtime
"""



from pathlib import Path
from datetime import datetime



class Showing:

    def __init__(self):
        pass

    def setStartTime(self, starttime):
        self.starttime = starttime

    def setHouse(self, housename: str):
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
        self.film
        self.dimension
        self.language
        self.price
        self.rating
        self.timelength
