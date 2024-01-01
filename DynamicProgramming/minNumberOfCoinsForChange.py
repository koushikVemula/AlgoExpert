def minNumberOfCoinsForChange(n, denoms):
    # Write your code here.
    if n==0 :
        return 0
    array = [n+1]*(n+1)
    ptr = 1
    for i in range(1,n+1) :
        if i in denoms :
            array[i] = 1
            continue
        else :
            for j in denoms :
                if i-j<=0 :
                    continue
                else :
                    array[i] = min(array[i],array[i-j]+1)
        print(i,array)
    if array[n]!= n+1 :
        return array[n]
    return -1
