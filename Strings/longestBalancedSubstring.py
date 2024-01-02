def longestBalancedSubstring(string):
    # Write your code here.
    llen = 0
    left = 0
    right = 0
    ct = 0
    while left < len(string) :
        #break condition for while loop
        if right == len(string) : 
            if ct > 0 :
                right = left + 1
                left = left + 1
                ct = 0
                continue
            break

        #operation on count
        if string[right] == "(" :
            ct +=1
        else :
            ct -=1

        #action depending on count
        if ct == 0 :
            print("sc ",string[left:right+1])
            llen = max(llen, right-left+1)
            right +=1
        elif ct < 0 :
            ct = 0
            left = right + 1
            right += 1
        else :
            right += 1
    return llen
