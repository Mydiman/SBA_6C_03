"""
Different colour
Reset --> Colour off + Black background + White words
B     --> Bold
On    --> Background
"""



class Colour:
	Reset: str = '\033[0m' + '\033[40m' + '\033[37m'
	Red: str = '\033[31m'
	Green: str = '\033[32m'
	Yellow: str = '\033[33m'
	Blue: str = '\033[34m'
	BWhite: str = '\033[1;37m'
	On_White: str = '\033[47m'
