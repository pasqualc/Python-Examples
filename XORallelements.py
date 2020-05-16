# This program takes a list of integers of any length, and then returns a list
# of the same size where B[i] is the XOR of all elements in A except for A[i].

while 1:
    x = input("Input: ")
    elements = x.split()
    result = []
    for i in range(0, len(elements)):
        xor = 0
        temp = elements.copy()
        temp.remove(elements[i])
        for j in range(0, len(temp)):
            xor ^= int(temp[j])
        result.append(xor)
    print(result)
    print("")
