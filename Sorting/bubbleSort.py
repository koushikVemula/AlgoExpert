def bubbleSort(array):
    # Write your code here.
    while True :
        swaps = 0
        for i in range(0,len(array)-1) :
            if array[i]>array[i+1] :
                array[i+1],array[i]=array[i],array[i+1]
                swaps+=1
        if swaps == 0 :
            break
    return array
