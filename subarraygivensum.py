def findSubstring(arr, sum):
    print(len(arr))
    for i in arr:
        list = []
        count = 0
        index = arr.index(i)
        while count < sum:
            count += arr[index]
            index += 1
            list.append(i)
            if count == sum:
                return list
            if index > len(arr):
                break
    return -1

while 1:
    sum = int(input("Sum: "))
    arr = [int(x) for x in input("Array: ").split()]
    print(findSubstring(arr, sum))
