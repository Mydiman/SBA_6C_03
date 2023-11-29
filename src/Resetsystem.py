"Delete all data"



from .CommondPath import commond_path



def reset_sys():
    from os import walk, path, unlink, mkdir
    from shutil import rmtree
    if path.exists(path.join(commond_path, 'Data')):
        for root, dirs, files in walk(path.join(commond_path, 'Data')):
            for f in files:
                unlink(path.join(root, f))
            for d in dirs:
                rmtree(path.join(root, d))
    else:
        mkdir(path.join(commond_path, 'Data'))
    mkdir(path.join(commond_path, 'Data', 'Account'))
    mkdir(path.join(commond_path, 'Data', 'House'))
    mkdir(path.join(commond_path, 'Data', 'Film'))
    mkdir(path.join(commond_path, 'Data', 'Showing'))
    mkdir(path.join(commond_path, 'Data', 'Showing', '__Film information'))
    mkdir(path.join(commond_path, 'Data', 'Showing', '__House information'))
    mkdir(path.join(commond_path, 'Data', 'Showing', '__Time information'))
    file_path = path.join(commond_path, 'Data', 'Account', 'admin.txt')
    f = open(file_path, "w")
    f.write("Username: admin\nPassword: pass")
    f.close()
    file_path = path.join(commond_path, 'Data', 'Account', 'user.txt')
    f = open(file_path, "w")
    f.write("Username: user\nPassword: bhjs")
    f.close()
    file_path = path.join(commond_path, 'Data', 'Account', 'admin_login_time.txt')
    f = open(file_path, "w")
    f.write("")
    f.close()
    file_path = path.join(commond_path, 'Data', 'Account', 'user_login_time.txt')
    f = open(file_path, "w")
    f.write("")
    f.close()
    file_path = path.join(commond_path, 'Data', 'House', 'housename.txt')
    f = open(file_path, "w")
    f.write("0\n")
    f.close()
    file_path = path.join(commond_path, 'Data', 'Film', 'filmname.txt')
    f = open(file_path, "w")
    f.write("0\n")
    f.close()
    file_path = path.join(commond_path, 'Data', 'Film', 'filmname.txt')
    f = open(file_path, "w")
    f.write("0\n")
    f.close()
    file_path = path.join(commond_path, 'Data', 'Showing', '__Film information', 'do_not_delete.txt')
    f = open(file_path, "w")
    f.write("")
    f.close()
    file_path = path.join(commond_path, 'Data', 'Showing', '__House information', 'do_not_delete.txt')
    f = open(file_path, "w")
    f.write("")
    f.close()
    file_path = path.join(commond_path, 'Data', 'Showing', '__Time information', 'Showingnum.txt')
    f = open(file_path, "w")
    f.write("0\n")
    f.close()
    file_path = path.join(commond_path, 'Data', 'Showing', '__Time information', 'Time.txt')
    f = open(file_path, "w")
    f.write("")
    f.close()
    file_path = path.join(commond_path, 'Data', 'Showing', 'Showing.txt')
    f = open(file_path, "w")
    f.write("")
    f.close()
    file_path = path.join(commond_path, 'Data', 'Showing', 'Missshowing.txt')
    f = open(file_path, "w")
    f.write("")
    f.close()
    file_path = path.join(commond_path, 'Data', 'Showing', 'Showingnum.txt')
    f = open(file_path, "w")
    f.write("")
    f.close()
