def countInversions(array):
    # Write your code here.
    l = []
    ans = 0
    print("array - ",array)
    for i in array[::-1] : 
        k=binarySearch(l,i,0,len(l)-1)
        l = l[0:k]+[i]+l[k:]
        ans += k
    return ans



def binarySearch(a, item, low, high):
    while (low <= high):
        mid = low + (high - low) // 2
        if (item > a[mid]):
            low = mid + 1
        else:
            high = mid - 1
    return low