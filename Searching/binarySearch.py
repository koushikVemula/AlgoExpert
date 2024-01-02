def binarySearch(array, target):
    # Write your code here.
    print(target,array)
    if len(array) == 1:
        if target!=array[0] :
            return -1
    n = len(array)//2
    if target == array[n] :
        return n
    elif target < array[n] :
        return binarySearch(array[0:n],target)
    else :
        k = binarySearch(array[n+1:],target)
        if k == -1 :
            return -1
        return n+1+k