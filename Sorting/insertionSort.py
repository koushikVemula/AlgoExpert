def insertionSort(array):
    # Write your code here.
    for i in range(0,len(array)) :
        array = insert(array,i)
    return array
    
def insert(array,position) :
    print(array[0:position])
    i = 0
    while i<position :
        if array[i] > array[position] :
            break
        i += 1
    array = array[0:i]+[array[position]]+array[i:position]+array[position+1:]
    return array
