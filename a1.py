# a1.py

# Starter code for assignment 1 in ICS 32 Programming with Software Libraries in Python

# Replace the following placeholders with your information.

# Rohit George Rarichan 
# raricha@uci.edu
# 36126645
from pathlib import Path

def direc_list(myPath):  #list_dir contains ['L', '/home/algol/ics32/lectures']
    for currentpath in myPath.iterdir():
        print(currentpath)

def recursive_list(myPath):  #searching for files inside a directory
    for currentpath in myPath.iterdir(): 
        if currentpath.is_file():
            print(currentpath)
        elif currentpath.is_dir():
            print(currentpath)
            recursive_list(currentpath)

def only_files(myPath):    #searching for files in the path
    for currentpath in myPath.iterdir():
        if currentpath.is_file():
            print(currentpath)

def file_search(myPath, filename):  #searching for files by name
    for currentpath in myPath.iterdir():
        if currentpath.is_file() and currentpath.name.lower() == filename.lower():
            print(currentpath)

def search_by_extension(myPath, ext):  #searching for files by their extensions
    for currentpath in myPath.iterdir():
        if currentpath.is_file() and currentpath.suffix.lower() == ext.lower():
            print(currentpath)

def search_by_extension_recursive(myPath, ext): #searching for files by extensions recursively
    for currentpath in myPath.iterdir():
        if currentpath.is_file() and currentpath.suffix.lower() == ext.lower():
            print(currentpath)
        elif currentpath.is_dir():
            search_by_extension_recursive(currentpath, ext)

def files_search_recursive(myPath, filename):  #searching for files by file names recursively
    for currentpath in myPath.iterdir():
        if currentpath.is_file() and currentpath.name.lower() == filename.lower():
            print(currentpath)
        elif currentpath.is_dir():
            files_search_recursive(currentpath, filename)

def create_file(path_init):    #creating a file 
    file = Path(path_init)
    my_file = file.open("w")
    my_file.close()

def delete_file(myPath):      #deleting a file
    try:
        myPath.unlink()
    except FileNotFoundError:
        print(f"File not found: {myPath}")

def read_file(myPath):        #reading the contents of a file 
    try:
        with myPath.open('r') as my_file:
            data = my_file.read()
            if not data:
                print("EMPTY")
            else:
                print(data)
    except FileNotFoundError:
        print(f"File not found: {myPath}")
    except Exception as e:
        print(f"Error reading file: {e}")

def main(Command):   #main function
    list_dir = Command.split(maxsplit = 1)
    myPath = Path(list_dir[1])
    if len(list_dir) == 2:
        if Command.startswith('L'):
            direc_list(myPath)
        elif Command.startswith('D'):
            myPath = Path(list_dir[1])
            delete_file(myPath)
        elif Command.startswith('R'):
            if list_dir[1][-4:] == ".dsu":
                myPath = Path(list_dir[1])
                read_file(myPath)
    elif len(list_dir) == 3:
        if list_dir[2] == '-r':
            recursive_list(myPath)
        elif list_dir[2] == '-f':
            only_files(myPath)
    elif len(list_dir) == 4:
        if list_dir[2] == '-s':
            filename = list_dir[3]
            file_search(myPath, filename)
        elif list_dir[2] == '-e':
            ext = list_dir[3]
            search_by_extension(myPath, ext)
        elif list_dir[2] == '-n' and Command.startswith('C'):
            Path_init = myPath / (list_dir[3] + ".dsu")
            create_file(Path_init)       
    elif len(list_dir) == 5:
        if list_dir[2] == '-r' and list_dir[3] == '-s':
            filename = list_dir[4]
            files_search_recursive(myPath, filename)
        elif list_dir[2] == '-r' and list_dir[3] == '-e':
            ext = list_dir[4]
            search_by_extension_recursive(myPath, ext)
        

if __name__ == "__main__":
    while True:
        Command = input("L to list the contents C to create a file D to delete a file R to read the contenst of a file (Q to quit)")
        if Command == 'Q':
            break
        elif Command.startswith('L') or Command.startswith('C') or Command.startswith('D') or Command.startswith('R'):
            main(Command)
        

