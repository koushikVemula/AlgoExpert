def optimalAssemblyLine(stepDurations, numStations):
    # Write your code here.
    minTime = max(stepDurations)
    maxTime = sum(stepDurations) 
    while True :
        cTime = ((maxTime-minTime)//2)+minTime
        [value,stations] = getTime(stepDurations, cTime, minTime)
        if value == minTime :
            return minTime
        if stations < numStations :
            maxTime = value
        elif stations > numStations :
            minTime = cTime + 1
        else :
            return value

def getTime(stepDurations,timeLimit, minTime) :
    [maxT, number] = check(stepDurations, timeLimit)
    while True:
        if maxT == minTime :
            break
        [newT, newNumber] = check(stepDurations, maxT-1)
        if newNumber == number:
            maxT = newT
        else:
            break
    return [maxT, number]

def check(stepDurations, limit) :
    stations = 0
    maxTime = 0
    cTime = 0
    print(maxTime,limit)
    for i in stepDurations :
        if cTime + i <= limit :
            cTime += i
            print("cTime",cTime)
        else :
            maxTime = max(maxTime,cTime)
            cTime = i
            stations += 1
    if cTime!=0 :
        maxTime = max(maxTime,cTime)
        stations+=1
    print("check details",maxTime,limit)
    return [maxTime,stations]
            
            
    
