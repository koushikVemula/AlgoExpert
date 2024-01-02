def shiftedBinarySearch(array, target):
    # Write your code here.
    pivot = findPivot(array)
    if target >= array[pivot] and target <= array[-1] :
        k = binarySearch(array[pivot:],target)
        if k==-1 :
            return -1
        return pivot + k
    else :
        return binarySearch(array[0:pivot],target)

def findPivot(array) :
    if len(array) == 1:
        return 0
    if len(array) == 2:
        if array[0] < array[1] :
            return 0
        return 1
    mid = len(array)//2
    if array[mid] < array[0] :
        if array[mid-1] > array[mid] :
            return mid
        return findPivot(array[0:mid])
    else :
        if array[mid+1] < array[mid] :
            return mid+1
        k=findPivot(array[mid+1:])
        return k+mid+1

def binarySearch(array,target) :
    print(array,target)
    if len(array) == 0:
        return -1
    if len(array) == 1:
        if array[0] == target :
            return 0
        return -1
    mid = len(array)//2
    if array[mid] == target :
        return mid
    elif array[mid] > target :
        return binarySearch(array[0:mid],target)
    else :
        k = binarySearch(array[mid+1:],target)
        if k == -1:
            return -1
        return mid+1+k