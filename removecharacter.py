# This program takes two strings and removes all characters that appear in the
# second string from the first string, then outputs the result

while 1:
    s1 = input("String 1: ")
    s2 = input("String 2: ")
    for c in set(s2):
        s1 = s1.replace(c, "")
    print(s1)
