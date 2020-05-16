def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

while 1:
    fileName = input("File name: ")
    print(file_len(fileName))
