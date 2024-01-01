def diceThrows(numDice, numSides, target):
    # Write your code here.
    storedResults = [[0]* (target+1) for _ in range(numDice+1)]
    storedResults[0][0] = 1

    for currentNumDice in range(1,numDice+1) :
        for currentTarget in range(0,target+1) :
            numWays = 0
            for currentNumSides in range(1, min(currentTarget, numSides) +1) :
                numWays += storedResults[currentNumDice-1][currentTarget-currentNumSides]
            storedResults[currentNumDice][currentTarget] = numWays
    return storedResults[numDice][target]
