def classPhotos(red, blue):
    # Write your code here.
    red.sort()
    blue.sort()
    if red[0] > blue[0] :
        l1 = blue
        l2 = red
    elif red[0] < blue[0] :
        l1 = red
        l2 = blue
    else :
        return False
    for i in range(0,len(red)) :
        if l1[i] >= l2[i] :
            return False
    return True
