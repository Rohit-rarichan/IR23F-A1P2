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


def main(Command):   #main function
    list_dir = Command.split()
    myPath = Path(list_dir[1])
    if len(list_dir) == 2:
        direc_list(myPath)
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
    elif len(list_dir) == 5:
        if list_dir[2] == '-r' and list_dir[3] == '-s':
            filename = list_dir[4]
            files_search_recursive(myPath, filename)
        elif list_dir[2] == '-r' and list_dir[3] == '-e':
            ext = list_dir[4]
            search_by_extension_recursive(myPath, ext)
        

if __name__ == "__main__":
    while True:
        Command = input("L to list the contents of the user specified directory (Q to quit)")
        if Command == 'Q':
            break
        elif Command.startswith('L'):
            main(Command)

