# This program takes an integer input, N,  and outputs the smallest power
# of 2 that is greater than or equal to N. For example, if you input 11, the
# output will be 16. Or if you input 7, the output will be 8.

while 1:
    n = int(input("Input N: "))
    if n < 2:
        print("N must be >= 2")
        continue
    x = 2
    while 1:
        if x >= n:
            break
        x *= 2
    print("Result = %d\n" % x)
