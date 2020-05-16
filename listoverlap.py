# List overlap: Print a list containing every value two lists, a and b,
# have in common (without overlap)
def overlapCheck(a, b):
    c = []
    for x in a:
        if x in b:
            if x in c:
                continue
            c.append(x)
    return c

# This method is more efficient than the above method at the expensve of
# more space used by converting the lists in to sets
def overlapCheck_set(a,b):
    set_a = set(a)
    set_b = set(b)
    return set_a.intersection(set_b)

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print(a)
print(b)
print(set(a) & set(b))
