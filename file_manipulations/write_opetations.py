def create_write():
    file = open('geeks.txt','w')
    file.write('Test results')
    file.close()

def append():
    file = open('geeks.txt','a')
    file.write('Adding more tests')
    file.close()
append()