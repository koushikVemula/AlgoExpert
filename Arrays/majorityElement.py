def majorityElement(array):
    # Write your code here.
    ans = array[0]
    ct = 1
    for i in array[1:] :
        if ct == 0 :
            ans = i
            ct = 1
            continue
        if i==ans :
            ct += 1
        else :
            ct -= 1   
    return ans
