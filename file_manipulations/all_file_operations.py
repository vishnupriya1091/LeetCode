import os


def create_write(file):
    try:
        f = open(file, 'w')
        f.write("This is a New file")
        f.close()
    except IOError:
        print(file + " cannot be created")


def readFile(file):
    try:
        with open(file, 'r') as f:
            s = f.read()
            print(type(s))
            print(s)
    except IOError:
        print("File not found")


def append(file):
    with open(file, 'a') as f:
        f.write('\nAppending to existing file')
        print("File has been appended")
        f.close()


def rename(file, new_filename):
    os.rename(file, new_filename)


def delete(new_filename):
    os.remove(new_filename)


if __name__ == '__main__':
    filename = "all_file_manipulations.txt"
    newfilename = 'all_file_operations.txt'
    create_write(filename)
    readFile(filename)
    append(filename)
    rename(filename, newfilename)
    delete(newfilename)
