# Times program takes an integer N and a bit position K, and sets that bit
# position in N to 1. For example, if N is 9 (0b1001) and K is 1, the output
# will be 11 (0b1011). The position at the far right is considered to be 0

while 1:
    n = int(input("Input N: "))
    k = int(input("Position: "))
    result = n | pow(2,k)
    print("-----\nN: \t\t{}".format(bin(n)))
    print("K: \t\t{}".format(bin(pow(2,k))))
    print("Result: {} \t{}\n".format(result, bin(result)))
