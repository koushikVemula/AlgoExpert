def threeNumberSort(array, order):
    # Write your code here.
    table = dict()
    for i in order :
        table[i] = 0
    for i in array :
        table[i]+= 1
    array = []
    for i in order :
        array += [i]*table[i]
    return array
