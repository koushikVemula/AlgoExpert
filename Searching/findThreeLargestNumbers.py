def findThreeLargestNumbers(array):
    # Write your code here.
    ans = []
    for i in array :
        if len(ans) < 3:
            ans = insert(ans,i,position(ans,i))
        else :
            if i > ans[0] :
                ans = insert(ans[1:],i,position(ans[1:],i))
        print(i,ans)
    return ans
    
def insert(array,element,pos) :
    return array[0:pos+1] + [element] + array[pos+1:]

def position(array,element) :
    if len(array) == 0:
        return -1
    elif len(array) == 1:
        if array[0] >= element :
            return -1
        return 0
    else :
        if element < array[0] :
            return -1
        if element >= array[0] and element <array[1] :
            return 0
        if element >= array[1] :
            return 1
        
