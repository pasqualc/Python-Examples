# This program will take an integer X between 0 and 9, and a range LB and UB
# and will return the number of times X appears as a digit within that range

while 1:
    lb = int(input("Lower Bound: "))
    ub = int(input("Upper Bound: "))
    x = input("X: ")
    count = 0
    for i in range(lb+1, ub):
        if x in str(i):
            count+=str(i).count(x)
    print(count)
    print("")
