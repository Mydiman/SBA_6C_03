"""
Load in
Log in ---> AdminVersion
       ---> UserVersion
"""



if __name__ == '__main__':
	input("\033[31mPlease run { __main__.py } in the root directory of this project\033[K")
	quit()



from os import path
from time import sleep
from sys import exc_info
from .ClearScreen import clearscreen
from .Colour import Colour
from .LogIn import log_in
from .UserVersion import user_version
from .AdminVersion import admin_version
from .Resetsystem import reset_sys



def main() -> None:
	clearscreen()
	print(Colour.Reset)
	login_version = 3
	byebye = 0
	error = 0
	if not path.exists(path.join(path.dirname(path.realpath(__file__)), 'Data')):
		reset_sys()
	while True:
		try:
			if error == 0:
				clearscreen()
				login_version = log_in()
			else:
				clearscreen()
				print(Colour.Red + "THERE IS AN EXCEPTION { " + exception_type.__name__ + " } DETECTED" + Colour.Reset)
				if exception_type.__name__ == "FileNotFoundError":
					reset_sys()
					login_version = 3
					print(Colour.Red + "SYSTEM RESETED" + Colour.Reset)
					input(Colour.Yellow + "ENTER TO CONTINUE" + Colour.Reset)
					print("Username of admin: admin")
					print("Password of admin: pass")
					print("Username of admin: user")
					print("Password of admin: bhjs")
					input(Colour.Yellow + "ENTER TO CONTINUE" + Colour.Reset)
				elif login_version == 1:
					input(Colour.Yellow + "ENTER TO GO BACK TO ADMIN MENU" + Colour.Reset)
				elif login_version == 2:
					input(Colour.Yellow + "ENTER TO GO BACK TO USER MENU" + Colour.Reset)
				else:
					input(Colour.Yellow + "ENTER TO CONTINUE" + Colour.Reset)
			error = 0
			if login_version == 1:
				clearscreen()
				byebye = admin_version()
				login_version = 3
				if byebye == 0:
					clearscreen()
					list_logout = ["\\", "|", "/", "-"]
					for i in range(0, 3):
						for j in list_logout:
							print("\rLoging out in {} seconds {}".format(3 - i, j), end = "")
							sleep(0.25)
				if byebye == 1:
					clearscreen()
					list_quit = ["\\", "|", "/", "-"]
					for i in range(0, 3):
						for j in list_quit:
							print("\rShuting down in {} seconds {}".format(3 - i, j), end = "")
							sleep(0.25)
					break
			elif login_version == 2:
				clearscreen()
				user_version()
				login_version = 3
				clearscreen()
				list_logout = ["\\", "|", "/", "-"]
				for i in range(0, 3):
					for j in list_logout:
						print("\rLoging out in {} seconds {}".format(3 - i, j), end = "")
						sleep(0.25)
		except:
			exception_type = exc_info() [0]
			error = 1
	exit()
