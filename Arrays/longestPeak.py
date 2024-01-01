def longestPeak(array):
    # Write your code here.
    if not array :
        return 0
    bval = array[0]
    peaks=[]
    for i in range(1,len(array)-1) :
        if array[i] > bval and array[i] > array[i+1] :
            peaks.append(i)
        bval = array[i]
    mpeakval = 0
    for i in peaks :
        pstart,pend = i,i
        while(pstart>=1) :
            bval = array[pstart]
            pstart = pstart - 1 
            if array[pstart] < bval :
                continue
            else :
                pstart = pstart + 1
                break
        while(pend<=len(array)-2):
            bval = array[pend]
            pend = pend + 1 
            if array[pend] < bval :
                continue
            else :
                pend = pend - 1
                break
        mpeakval = max(mpeakval,pend-pstart+1)
    return mpeakval
            