def bestSeat(seats):
    # Write your code here.
    if 0 not in seats :
        return -1
    zmstart = -1
    zm = -1
    zcstart = -1
    zc = 0
    
    for i in range(0,len(seats)) : 
        if seats[i]==0 :
            if zcstart == -1 :
                zcstart = i
                zc = 1
            else :
                zc = zc +1
        elif seats[i]==1 :
            if zcstart == -1 :
                zc = -1
                continue
            else :
                if zc > zm :
                    zm = zc
                    zmstart = zcstart
                zc = -1
                zcstart = -1
                
    if zm %2 == 0 :
        return zmstart + int(zm/2) - 1
    else :
        return zmstart + int(zm/2)
