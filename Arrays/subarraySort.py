def check(narray,i) :
    if not narray :
        return 0
    val=len(narray)
    for ele in narray[::-1] :
        if i>=ele :
            return val
        val -= 1
    return 0
    
def subarraySort(array):
    # Write your code here.
    print(array)
    narray= []
    cstart = 1000000
    cend = 1000000
    for i in range(0,len(array)) :
        pos = check(narray,array[i])
        if pos != len(narray) :
            cstart = min(pos,cstart)
            cend = i
        narray.insert(pos,array[i])
    if cstart == 1000000 :
        return [-1,-1]
    else :
        return [cstart,cend]
    