def tandemBicycle(red, blue, fastest):
    # Write your code here.
    red.sort()
    blue.sort()
    if fastest :
        red.reverse()
    ans = 0
    for i in range(0,len(red)) :
        ans = ans + max(red[i],blue[i])
    return ans
