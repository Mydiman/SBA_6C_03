"""
Load in
Log in ---> AdminVersion
       ---> UserVersion
"""



if __name__ == '__main__':
	from Colour import Colour
	input(Colour.Red + "Please run { __main__.py } in the root directory of this project" + Colour.Reset)
	quit()



from time import sleep
from sys import exc_info
from traceback import print_tb
from .ClearScreen import clearscreen
from .Colour import Colour
from .LogIn import log_in
from .UserVersion import user_version
from .AdminVersion import admin_version



def main() -> None:
	clearscreen()
	print(Colour.Reset)
	#Don't forgot check data folder exist!!!
	login_version = 3
	error = 0
	while True:
		#try:
			if error == 0:
				login_version = log_in()
			else:
				clearscreen()
				print(Colour.Red + "THERE IS AN EXCEPTION { " + exception_type.__name__ + " } DETECTED" + Colour.Reset)
				print(print_tb(exception_line))
				if login_version == 1:
					input(Colour.Yellow + "ENTER TO GO BACK TO ADMIN MENU" + Colour.Reset)
				elif login_version == 2:
					input(Colour.Yellow + "ENTER TO GO BACK TO USER MENU" + Colour.Reset)
				else:
					input(Colour.Yellow + "ENTER TO CONTINUE" + Colour.Reset)
			clearscreen()
			error = 0
			if login_version == 1:
				if admin_version() == 1:
					list_quit = ["\\", "|", "/", "-"]
					for i in range(0, 3):
						for j in list_quit:
							print("\rShuting down in {} seconds {}".format(3 - i, j), end = "")
							sleep(0.25)
					exit()
			elif login_version == 2:
				user_version()
		#except:
		#	exception_type = exc_info() [0]
		#	exception_line = exc_info() [2]
		#	error = 1