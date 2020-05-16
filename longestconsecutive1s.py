# This program takes an integer and returns the longest consecutive string of
# 1s present in the binary representation of the number

while 1:
    x = int(input("Input: "))
    print(format(x, '#010b'))
    count = max = 0
    while x > 0:
        if (x & 1) == 1:
            count += 1
        else:
            count = 0
        if count > max:
            max = count
        x = x >> 1
    print("Result: %d\n" % max)
