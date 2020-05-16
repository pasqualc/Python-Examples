# Given a Byte of data, this program will swap the first and the second nibble
# of the number and return the new resulting Byte

while 1:
    x = int(input("Input: "))
    print("Binary:  " + format(x, '#010b'))
    x2 = x
    x = x >> 4
    x2 = x2 << 4
    xor = (x ^ x2) % 256
    print("Swapped: " + format(xor, '#010b') + "\n")
