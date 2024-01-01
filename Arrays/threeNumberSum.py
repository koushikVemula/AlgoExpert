def threeNumberSum(array, targetSum):
    # Write your code here.
    array.sort()
    ans = []
    for k in range(0,len(array)-2) :
        i,j=k+1,len(array)-1
        while(i<j) :
            if array[i] + array[j] + array[k] == targetSum :
                if [array[k],array[i],array[j]] not in ans :
                    ans.append([array[k],array[i],array[j]])
                i = i+1
            elif array[i] + array[j] + array[k] > targetSum :
                j = j-1
            else :
                i = i+1
    return ans