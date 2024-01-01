def zeroSumSubarray(nums):
    # Write your code here.
    sums = [0]
    for i in nums :
        nval = sums[len(sums)-1]+i
        if nval in sums : 
            return True
        sums.append(nval)
    return False