def dijkstrasAlgorithm(start, edges):
    # Write your code here.
    edgeMap = dict()
    minDistance = [float("inf") for _ in range(0,len(edges))]
    minDistance[start] = 0
    visitedNodes = []
    availableNodes = [start]
    while availableNodes :
        cNode = availableNodes.pop()
        if cNode in visitedNodes :
            continue
        for [i,j] in edges[cNode] :
            temp  = minDistance[cNode]+j
            if temp < minDistance[i] :
                if i in visitedNodes :
                    visitedNodes.remove(i)
                minDistance[i] = temp
            availableNodes.append(i)
        visitedNodes.append(cNode)
    ans = []
    for i in minDistance :
        if i == float("inf") :
            ans.append(-1)
        else :
            ans.append(i)
    return ans
