# This program takes an Integer as input, displays the binary representation
# of that integer, and then outputs the number of 0s and 1s found in the
# binary representation (up to the highest set bit, so we don't have infinite
# zeroes). For example, if input is 9 (0b1001), output will show 2 1s and 2 0s.

# Brian Kernighan's Algorithm (Recursive Version)
def countSetBitsR(n):
    if (n == 0):
        return 0
    else:
        return 1 + countSetBits(n & (n - 1))

# Brian Kernighan's Algorithm (Iterative Version)
def countSetBits(n):
    count = 0
    while(n > 0):
        n &= (n-1)
        count += 1
    return count

# x holds one set digit at a time
# starting from LSB to MSB of n.
def countUnsetBits(n):
    count = 0
    x = 1
    while(x < n + 1):
        if ((x & n) == 0):
            count += 1
        x = x << 1
    return count

while 1:
    n = int(input("Input: "))
    print("Binary: " + bin(n))
    print("Count of 1s: %d" % countSetBitsR(n))
    print("Count of 0s: %d\n" % countUnsetBits(n))
