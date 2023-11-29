"""
Clear screen
'Windows' --> 'cls'
'linux' --> 'clear'
'macos' --> 'clear'
"""



from platform import system as platform_system
from os import system as os_system



def clearscreen() -> None:
    print()
    if platform_system() == "Windows":
        os_system('cls')
    else:
        os_system('clear')