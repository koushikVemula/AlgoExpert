def largestRange(array):
    # Write your code here.
    array.sort()
    cstart = -1
    crange = -1
    mstart = -1
    mrange = -1
    for i in array :
        if crange == -1 : 
            cstart = i
            crange = 0
        else :
            if i == cstart + crange + 1 :
                crange += 1
            elif i == cstart + crange :
                continue
            else :
                if crange > mrange :
                    mstart = cstart
                    mrange = crange
                cstart = i
                crange = 0
    if crange > mrange :
        mstart = cstart
        mrange = crange
    return [mstart,mstart+mrange]
