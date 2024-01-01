def maxSumIncreasingSubsequence(array):
    # Write your code here.
    sums = [None]*len(array)
    sequence = [None]*len(array)

    for i in range(0,len(array)) :
        sums[i] = array[i]
        for j in range(0,i) :
            if array[i]>array[j] :
                if sums[i]<sums[j]+array[i] :
                    sums[i]=sums[j]+array[i]
                    sequence[i] = j
    maxSum = sums[0]
    maxIndex = 0
    for i in range(1,len(array)) :
        if maxSum < sums[i] :
            maxSum = sums[i]
            maxIndex = i
    clist = [array[maxIndex]]
    csequence = sequence[maxIndex]
    while csequence!=None :
        clist.append(array[csequence])
        csequence = sequence[csequence]
    clist.reverse()
    return [maxSum,clist]
    