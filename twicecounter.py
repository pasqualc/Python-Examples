# Given a list of words, this program will return the number of words that
# appear exactly twice in the input file.

input = open("twicecounter.txt", "r")
cases = input.readline().split()
dict = {}
for x in cases:
    if x in dict:
        dict[x] = int(dict[x] + 1)
        continue
    dict[x] = 1
z = 0
for y in dict.values():
    if y == 2:
        z = z + 1
print(z)
