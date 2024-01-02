def medianOfTwoSortedArrays(arrayOne, arrayTwo):
    # Write your code here.
    idxOne, idxTwo =0, 0
    middleIdx = (len(arrayOne)+len(arrayTwo)-1) //2
    while idxOne + idxTwo < middleIdx :
        if idxOne >= len(arrayOne) :
            idxTwo += 1
        elif idxTwo >= len(arrayTwo) :
            idxOne += 1
        elif arrayOne[idxOne] <arrayTwo[idxTwo] :
            idxOne += 1
        else :
            idxTwo += 1
    if (len(arrayOne) + len(arrayTwo)) %2 == 0 :
        areBothValuesArrayOne = idxTwo >= len(arrayTwo) or (idxOne + 1 < len(arrayOne) and arrayTwo[idxTwo] >arrayOne[idxOne + 1])
        areBothValuesArrayTwo = idxOne 
