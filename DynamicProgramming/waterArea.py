def waterArea(heights):
    # Write your code here.
    if heights== [] :
        return 0
    for i in range(0,len(heights)) :
        if heights[i] != 0 :
            break
    for j in range(len(heights)-1,-1,-1) :
        if heights[j] != 0 :
            break
    leftVal = heights[i]
    rightVal = heights[j]
    val = 0
    while i<j-1 :
        if leftVal < rightVal :
            i += 1
            if heights[i] < leftVal :
                val += leftVal - heights[i]
            else :
                leftVal = heights[i]
        else :
            j -= 1
            if heights[j] < rightVal :
                val += rightVal - heights[j]
            else :
                rightVal = heights[j]
    return val
                
            
