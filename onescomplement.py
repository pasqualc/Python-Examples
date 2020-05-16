# This program takes an integer as an input, and outputs the one's complement
# of that integer in binary. It does this by putting the binary representation
# of that number in a list, and then iterates over the list, swapping each
# 1 for a 0 and each 0 for a 1.

while 1:
    x = int(input("Input: "))
    print("Binary: " + format(x, '#010b'))
    listx = [int(d) for d in str(bin(x))[2:]]
    length = len(listx)
    for i in range(len(listx)):
        if listx[i] == 1:
            listx[i] = 0
        else:
            listx[i] = 1
    z = bin(int(''.join(map(str, listx)), 2))
    z = int(z, 2)
    print("Result: " + format(z, '#010b'))
    print("")
