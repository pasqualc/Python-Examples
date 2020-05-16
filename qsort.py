def quickSort(alist):
  quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
  if first < last:
      piv = partition(alist,first,last)
      print("first = " + str(alist[first]) +", last = " + str(alist[last]))
      print(alist)
      quickSortHelper(alist,first,piv-1)
      quickSortHelper(alist,piv+1,last)

def partition(a, start, end):
  i = start + 1
  piv = a[start+1]
  print("piv = " + str(piv))
  for j in range(start+1, end+1):
      if a[j] < piv:
          a[i],a[j] = a[j],a[i]     #swap i and j
          i+=1                      #increment left pointer
  a[start],a[i-1] = a[i-1],a[start] #swap a[start] and a[i-1]
  return i-1

def main():
    arr = [23,32,18,8,27,9,30,98,14,45,0,99,47,43,23,123,75,6,19,85]
    print("Starting array:")
    print(arr)
    print("Executing quickSort()...")
    quickSort(arr)
    print("After quickSort():")
    print(arr)
    return

if __name__ == "__main__":
    main()
