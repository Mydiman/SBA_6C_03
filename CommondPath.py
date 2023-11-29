"""import commond_path"""



from os import path



def dir_name() -> path:
    commond_path = path.dirname(__file__)
    return commond_path



commond_path = dir_name()