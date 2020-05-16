def getSum(arr):
    daSum = 0
    for x in range(len(arr)):
        daSum += arr[x]
    return daSum

def findSubO2(arr):
    n = len(arr)
    localSum = 0
    globalSum = 0
    for i in range(0, n - 1):
        for j in range(i, n - 1):
            localSum = getSum(arr[i:j])
            globalSum = max(localSum, globalSum)
    return globalSum

if __name__ == "__main__":
    daArray = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(findSubO2(daArray))
