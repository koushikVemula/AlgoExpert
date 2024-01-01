def longestSubarrayWithSum(array, targetSum):
    # Write your code here.
    print(array)
    i,j=0,0
    sum = array[0]
    cans = []
    clen = 0
    while(i<len(array) and j<len(array)) :
        if (sum<targetSum) :
            j+=1
            if j!=len(array) :
                sum = sum+array[j]
        elif sum == targetSum :
            if j-i+1 > clen :
                cans = [i,j]
                clen = j-i+1
            if(j == len(array)-1) :
                break
            elif(array[j+1] == 0) :
                j +=1
            else :
                sum = sum - array[i]
                i+=1
        else :
            sum = sum - array[i]
            i+=1
    return cans
