# This program takes an input N along with a range, L and R. N is any integer
# and L and R are the range of bits to toggle. L has to be greater than R since
# we count from the right. Example: If the input is 15 (0b1111) and the range is
# 0 to 2, output will be 8 (0b1000)

while 1:
    n = int(input("N:"))
    r = int(input("R:"))
    l = int(input("L:"))
    if l < r:
        print("L must be greater  than R\n")
        continue
    print("Input: \t\t{}".format(bin(n)))
    for i in range(r, l+1):
        n = n ^ pow(2, i)
    print("Output: \t{}\n".format(bin(n)))
