def isMonotonic(array):
    print(array)
    # Write your code here.
    if len(array) <=2 :
        return True
    if (array[len(array)-1]-array[0])!=0 :
        dir = (array[len(array)-1]-array[0])/abs((array[len(array)-1]-array[0]))
    else :
        dir = 0
    if dir == 0 :
        for i in array :
            if i!=array[0] :
                return False
    else :
        for i in range(0,len(array)-1) :
            if (array[i+1]-array[i])*dir < 0 :
                return False
    return True
    
