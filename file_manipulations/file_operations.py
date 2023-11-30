import json


# Read 1st record from a test file using json to load which converts json into dict
def read_load_json():
    with open('test_data.json', 'r') as f:
        s = json.load(f)
        print(s[0])


def open_alias_print():
    # Read records printing each line in a test file.
    # The open command will open the file in the read mode and the for loop will print each line present in the file.
    with open('test_data.json', 'r') as f:
        for each in f:
            print(each)


def open_file_read():
    # In this example, we will extract a string that contains
    # all characters in the file then we can use file.read().
    # reading first 15 characters
    f = open('test_data.json', 'r')
    print(f.read(15))


def open_csv_read():
    f = open('MOCK_DATA.csv', 'r')
    print(f.read())


def open_csv_alias_each():
    with open('MOCK_DATA.csv', 'r') as f:
        for each in f:
            print(each)


def split_lines():
    with open('MOCK_DATA.csv', 'r') as f:
        for i in f:
            word = i.split()
            print(word)

