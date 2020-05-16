# This program takes a list of integers as input, and outputs the sum of all
# the bit differences between all possible pairs of ints. Example: If input
# is [1, 3, 5], the program will take every possible pair such as (1, 5), (5,1),
# (1, 3), etc... and finds the number of bit differences in each pair, and then
# output the sum of all differences. The result for this example would be 8.

import itertools
while 1:
    s = input("Input: ")
    mylist = s.split()
    mylist = [int(x) for x in mylist]       # convert list of strings to ints
    diffs = []
    for p in itertools.combinations(mylist, 2):
        count = 0
        x = p[0]
        y = p[1]
        while x > 0 or y > 0:
             # check rightmost bits for difference
            if (x % 2) != (y % 2):
                count += 2
            x = x >> 1
            y = y >> 1
        diffs.append(count)
    x = sum(diffs)
    print("Result: %d\n" % x)
