def selectionSort(array):
    # Write your code here.
    for i in range(0,len(array)) :
        minPosition = i
        for j in range(i,len(array)) :
            if array[j] < array[minPosition] :
                minPosition = j
        array[i],array[minPosition]=array[minPosition],array[i]
    return array