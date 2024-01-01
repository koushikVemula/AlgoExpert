def twoNumberSum(array, targetSum):
    array.sort()
    i,j=0,len(array)-1
    while(i<j) :
        if (array[i]+array[j]) == targetSum :
            return [array[i],array[j]]
        elif (array[i]+array[j]) > targetSum :
            j = j-1
        else :
            i = i+1
    return []        
    
