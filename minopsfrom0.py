# This program takes an integer N and returns the minimum number of math
# operations it would take to go from 0 to N, given that the only allowed
# operations are adding 1 and multiplying by 2.

while 1:
    x = int(input("X: "))
    count = 0
    while x != 0:
        if (x % 2) == 0:
            x /= 2
        else:
            x -= 1
        count += 1
    print("Result: %d\n" % count)
