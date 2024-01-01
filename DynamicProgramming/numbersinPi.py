def numbersInPi(pi, numbers):
    # Write your code here.
    numbersTable = {number:True for number in numbers}
    minSpaces = getMinSpaces(pi, numbersTable, dict(), 0)
    if minSpaces == float("inf") :
        return -1
    else :
        return minSpaces
    

def getMinSpaces(pi,numbersTable, cache, idx) :
    if idx == len(pi) :
        return -1
    if idx in cache:
        return cache[idx]
    minSpaces = float("inf")
    for i in range(idx,len(pi)) :
        prefix = pi[idx:i+1]
        if prefix in numbersTable :
            minSpacesInSuffix = getMinSpaces(pi, numbersTable, cache, i+1)
            minSpaces = min(minSpaces,minSpacesInSuffix +1)
    cache[idx] = minSpaces
    return cache[idx]