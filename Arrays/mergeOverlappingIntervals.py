def sortKey(arr):
    return arr[0]

def merge(l1, l2):
    return [min(l1[0], l2[0]), max(l1[1], l2[1])]

def mergeOverlappingIntervals(intervals):
    sIntervals = sorted(intervals, key=sortKey)
    olen = 0
    nlen = 0
    while True:
        olen = len(sIntervals)
        nlen = olen
        i = 0
        while i < nlen-1:
            if sIntervals[i][1] >= sIntervals[i+1][0]:
                l1 = sIntervals.pop(i)
                l2 = sIntervals.pop(i)
                nl = merge(l1, l2)
                sIntervals.insert(i, nl)
                nlen -= 1
            else:
                i += 1
        if olen == nlen:
            break
    return sIntervals
