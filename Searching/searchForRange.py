def searchForRange(array, target):
    # Write your code here.
    k = binarySearch(array,target)
    if k== -1 :
        return [-1,-1]
    kl = binaryLeft(array[0:k+1],target)
    kr = k+binaryRight(array[k:],target)
    return [kl,kr]

def binaryLeft(array,target) :
    if len(array) == 1 :
        return 0
    mid = len(array)//2
    if array[mid] == target :
        if array[mid-1] == target :
            return binaryLeft(array[0:mid],target)
        else :
            return mid
    elif array[mid] < target :
        return mid + 1 + binaryLeft(array[mid+1:],target)

def binaryRight(array,target) :
    if len(array) == 1 :
        return 0
    if len(array) == 2:
        if array[1]==target :
            return 1
        else :
            return 0
    mid = len(array)//2
    if array[mid] == target :
        if array[mid+1] == target :
            return mid+1+binaryRight(array[mid+1:],target)
        else :
            return mid
    elif array[mid] > target :
        return binaryRight(array[:mid],target)

def binarySearch(array,target) :
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