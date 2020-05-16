# This program takes two integers and outputs the position of the
# rightmost different bit. For example, if you input 14 (0b1110) and
# 12(0b1100), the output will be position 2.

while 1:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    print(bin(num1) + "\t" +bin(num2))
    num3 = num1 ^ num2
    if num3 == 0:
        print("No difference")
        continue
    counter = 1
    while 1:
        if (num3 & 1) == 1:
            break
        counter+=1
        num3 = num3 >> 1
    print("Rightmost different bit position: %d" % counter)
