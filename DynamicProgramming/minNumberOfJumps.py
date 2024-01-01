def minNumberOfJumps(array):
    # Write your code here.
    # not a better dynamic programming
    data = [len(array) for i in range(0,len(array))]
    data[0] = 0
    for i in range(1,len(array)) :
        for j in range(0,i) :
            if i-j > array[j] :
                continue
            data[i] = min(data[i],data[j]+1)
    print(data)
    return data[-1]
