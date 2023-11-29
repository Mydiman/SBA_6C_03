"""Send warning for changes in showings"""



from os import path, rename
from datetime import datetime, timedelta
from .CommondPath import commond_path
from .ClearScreen import clearscreen
from .Colour import Colour
from .CheckDatetime import check_datetime
from .Seatingplan import print_plan
from .UpdateDatetimeAll import update_status



def warning_204():
    