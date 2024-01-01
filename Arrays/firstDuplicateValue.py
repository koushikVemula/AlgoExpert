def firstDuplicateValue(array):
    # Write your code here.
    check = set()
    for i in array :
        if i in check :
            return i
        else :
            check.add(i)
    return -1
