# This program takes a string as input and outputs the minimum number of changes
# required to make every character in the string unique. This is done using
# python's Sets, which are able to take a string and automatically put every
# distinct character into a list, removing duplicates.

while 1:
    s = input("Input: ")
    sset = set(s)
    print("Result: %d\n" % (len(s) - len(sset)))
