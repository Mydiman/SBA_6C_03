"""
Different colour
Reset --> Colour off
B     --> Bold
On    --> Background
"""



if __name__ == '__main__':
	input("\033[31mPlease run { __main__.py } in the root directory of this project\033[K")
	quit()



class Colour:
	Reset: str = '\033[0m\033[K'
	Red: str = '\033[31m'
	Green: str = '\033[32m'
	Yellow: str = '\033[33m'
	Blue: str = '\033[34m'
	BWhite: str = '\033[1;37m\033[0m\033[K'
	OnWhite: str = '\033[47m\033[0m\033[K'
	Highlight: str = '\033[7m'
	Underline: str = '\033[4m'