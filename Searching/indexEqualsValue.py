def indexEqualsValue(array):
    # Write your code here.
    return binarySearch(0,len(array),array)

def binarySearch(startIdx,endIdx,array) :
    if startIdx == endIdx :
        return -1
    if startIdx == endIdx -1 :
        if array[startIdx] == startIdx :
            return startIdx
        else :
            return -1
    if startIdx == endIdx -2 :
        if array[startIdx] == startIdx :
            return startIdx
        elif array[startIdx+1] == startIdx+1 :
            return startIdx+1
        else :
            return -1
    mid = ((endIdx - startIdx) // 2) + startIdx
    if array[mid] == mid :
        return binarySearch(startIdx,mid+1,array)
    elif array[mid] < mid :
        return binarySearch(mid,endIdx,array)
    else :
        return binarySearch(startIdx,mid,array)