def radixSort(array):
    # Write your code here.
    if array == [] :
        return []
    maxValue = max(array)
    digits = 0
    while maxValue > 0 :
        maxValue = maxValue//10
        digits+=1
    for i in range(0,digits) :
        table = dict()
        for x in range(0,10) :
            table[x] = []
        for j in array :
            m = j //(10 ** i)
            digit = m%10
            table[digit].append(j)
        array = []
        for x in range(0,10) :
            array = array + table[x]
    return array