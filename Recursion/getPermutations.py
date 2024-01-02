def getPermutations(array):
    # Write your code here.
    if array == [] :
        return []
    ans = []
    for i in range(0,len(array)) :
        getP(array[0:i]+array[i+1:],[array[i]],ans)
    return ans

def getP(array,carray,ans) :
    if array == [] :
        ans.append(carray)
    else :
        for i in range(0,len(array)) :
            carray_copy = carray + [array[i]]
            getP(array[0:i] + array[i + 1:], carray_copy, ans)
            