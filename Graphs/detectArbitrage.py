import math
def detectArbitrage(exchangeRates):
    # Write your code here.
    logExchangeRates = convert(exchangeRates)
    return belManFord(logExchangeRates,0)

def convert(matrix) :
    ans = []
    for i in range(0,len(matrix)) :
        arow = []
        for j in range(0,len(matrix[i])) :
            arow.append(-1*math.log10(matrix[i][j]))
        ans.append(arow)
    return ans

def belManFord(graph, start) :
    distances = [float('inf') for _ in range(len(graph))]
    distances[start] = 0
    for _ in range(len(graph)-1) :
        if not relaxEdges(graph, distances) :
            return False

    return relaxEdges(graph, distances)


def relaxEdges(graph, distances) :
    updated = False
    # for sourceI
    for i in range(0,len(graph)) :
        for j in range(0,len(graph[i])) :
            latestDistance = distances[i]+graph[i][j]
            if latestDistance < distances[j] :
                updated = True
                distances[j] = latestDistance
    return updated


