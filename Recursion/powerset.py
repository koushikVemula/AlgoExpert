def powerset(array):
    # Write your code here.
    ans = []
    for i in range(len(array)+1) :
        cans = []
        getP(array,[],cans,i)
        for i in cans :
            ans.append(i)
    return ans

def getP(array,carray,cans,length) :
    if length == 0 :
        cans.append(carray.copy())
    else :
        for i in range(0,len(array)) :
            carray_copy = carray + [array[i]]
            getP(array[i+1:],carray_copy,cans,length-1)
