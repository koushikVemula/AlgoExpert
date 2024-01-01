def maxSubsetSumNoAdjacent(array):
    # Write your code here.
    if array == [] :
        return 0
    values = [0]*len(array)
    values[0] = array[0]
    if len(array) == 1 :
        return values[0]
    values[1] = max(array[0],array[1])
    for i in range(2,len(values)) :
        values[i] = max(values[i-1],values[i-2]+array[i])
    return values[len(values)-1]
