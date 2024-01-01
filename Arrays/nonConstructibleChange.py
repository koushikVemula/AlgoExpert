def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    if not coins :
        return 1
    elif coins[0]!=1 :
        return 1
    min = 1
    for i in coins[1:] :
        if i>min+1 :
            return min+1
        else:
            min = min + i
    return min+1
