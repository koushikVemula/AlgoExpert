def arrayOfProducts(array):
    # Write your code here.
    maxproduct = 1
    if 0 not in array :
        for i in array :
            maxproduct = maxproduct * i
        ans= []
        for i in array :
            ans.append(maxproduct/i)
        return ans
    else :
        if array.count(0) > 1 :
            return [0]*len(array)
        array2 = array.copy()
        array2.pop(0)
        print(array2)
        for i in array2 :
            maxproduct = maxproduct * i
        ans= []
        for i in array :
            print(i)
            if i == 0 :
                ans.append(maxproduct)
            else :
                ans.append(0)
        return ans