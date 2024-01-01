def missingNumbers(nums):
    # Write your code here.
    l = len(nums) + 2
    ans=[]
    for i in range(1,l+1):
        if i not in nums :
            ans.append(i)
    return ans
    
