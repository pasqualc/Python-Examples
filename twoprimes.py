# This program takes an even Integer > 2 as input, and outputs two prime numbers
# whose sum equals that integer. "Goldbach's Conjecture"

def isPrime(n):
    # Corner case
    if n <= 1:
        return False
    # Check from 2 to n-1
    for i in range(2, n):
        if n % i == 0:
            return False;
    return True

while 1:
    x = int(input("Input: "))
    if x <= 2 or x % 2 == 1:
        print("Integer must be even and > 2")
        continue
    for i in range(3, x):
        if isPrime(i) and isPrime(x-i):
            print("(" + str(i) + " , " + str(x-i) + ")")
            break   # remove if you want to see all combinations!
