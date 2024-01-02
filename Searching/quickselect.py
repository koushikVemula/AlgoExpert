def quickselect(array, k):
    # Write your code here.
    pivotValue = array[k-1]
    i = 0
    leftArray,rightArray = [],[]
    for i in array[0:k-1]+array[k:] :
        if i < pivotValue :
            leftArray.append(i)
        else :
            rightArray.append(i)
    leftLen = len(leftArray)
    if leftLen == k-1 :
        return pivotValue
    elif leftLen > k-1 :
        return quickselect(leftArray, k)
    else :
        return quickselect(rightArray,k-leftLen-1)