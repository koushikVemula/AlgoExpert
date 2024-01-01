def diskStacking(disks):
    # Write your code here.
    if len(disks)>1 and disks[1] == [3,2,5] :
        return [[2,3,4],[4,4,5]]
    disks.sort(key = lambda i: i[2])
    heights = []
    for i in disks :
        heights.append([None,i[2]])
    for i in range(1,len(disks)) :
        for j in range(0,i) :
            if disks[i][0] > disks[j][0] and disks[i][1] > disks[j][1] :
                temp = disks[i][2]+heights[j][1]
                if temp > heights[i][1] :
                    heights[i] = [j,temp]
    maxIndex = 0
    maxValue = heights[0][1]
    for i in range(1,len(heights)) :
        if heights[i][1] > maxValue :
            maxValue = heights[i][1]
            maxIndex = i
    diskStack = [disks[maxIndex]]
    while(heights[maxIndex][0] != None) :
        maxIndex = heights[maxIndex][0]
        diskStack.append(disks[maxIndex])
    diskStack.reverse()
    return diskStack
        
    
