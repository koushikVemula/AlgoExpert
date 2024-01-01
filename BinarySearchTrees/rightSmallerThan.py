def rightSmallerThan(array):
    # Write your code here.
    carray = []
    j = 0
    for i in array :
        carray.append([i,j])
        j+=1
    carray = sorted(carray, key = lambda x:x[0]*10000+x[1])
    ans = []
    j = 0
    print(carray)
    for i in array :
        k = binary(carray,i,j)
        j+=1
        carray = carray[:k] + carray[k+1:]
        ans.append(k)
    return ans

def binary(array,value,order) :
    i = 0
    j = len(array)-1
    while i<=j :
        mid = int((i+j)/2)
        if array[mid][0] == value :
            if array[mid][1] < order :
                i = mid+1
            elif array[mid][1] > order :
                j = mid-1
            else :
                return mid
        elif array[mid][0] < value :
            i = mid+1
        else :
            j = mid-1