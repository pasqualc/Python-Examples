# This program will take integers and add them to a "stream" of data, and
# output the new median of the entire stream after each insert.

stream = []
while 1:
    stream.append(int(input("Insert: ")))
    sortStream = stream.copy()
    sortStream.sort()
    if len(stream) == 1:
        median = sortStream[0]
    elif len(stream) == 2:
        median = (sortStream[0] + sortStream[1])/2
    elif len(stream) % 2 == 1:
        median = sortStream[int(len(sortStream)/2)]
    else:
        i = sortStream[int(len(sortStream)/2)]
        i2 = sortStream[(int(len(sortStream)/2))-1]
        median = (i+i2)/2
    print("Median: %d " % median, end = '')
    print(stream)
