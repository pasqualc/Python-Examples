# This program will take an array and a size of rotation as input. The Output
# will be that array "rotated" by the specified amount. For example, if the Input
# is [1, 2, 3, 4, 5] and size of rotation is 2, output is [3, 4, 5, 1, 2]

while 1:
    array = input("Array: ")
    list = array.split()
    size = int(input("Size of rotation: "))
    print(list)
    for i in range(0, size):
        list.append(list.pop(0))
    print(list)
    print("")
