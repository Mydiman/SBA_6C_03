"""
Clear screen
'Windows' --> 'cls'
'linux' --> 'clear'
'macos' --> 'clear'
"""



if __name__ == '__main__':
	input("\033[31mPlease run { __main__.py } in the root directory of this project\033[K")
	quit()
     

     
from platform import system as platform_system
from os import system as os_system



def clearscreen() -> None:
    print()
    if platform_system() == "Windows":
        os_system('cls')
    else:
        os_system('clear')