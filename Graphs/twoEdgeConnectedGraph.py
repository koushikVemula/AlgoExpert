def twoEdgeConnectedGraph(edges):
    # Write your code here.
    if len(edges) == 0:
        return True
    arrivalTimes = [-1] * len(edges)
    start = 0

    if getMinArrivalTimeOfAncestors(start,-1,0,arrivalTimes,edges)==-1:
        return False

    if -1 in arrivalTimes :
        return False
    return True

def getMinArrivalTimeOfAncestors(cVertex,parent,cTime,arrivalTimes,edges) :
    arrivalTimes[cVertex] = cTime
    minimumArrivalTime = cTime
    for destination in edges[cVertex] :
        if arrivalTimes[destination] == -1:
            minimumArrivalTime = min(minimumArrivalTime,getMinArrivalTimeOfAncestors(
                destination,cVertex,cTime+1,arrivalTimes,edges))
        elif destination!= parent :
            minimumArrivalTime = min(minimumArrivalTime,arrivalTimes[destination])
    if minimumArrivalTime == cTime and parent!= -1 :
        return -1

    return minimumArrivalTime
