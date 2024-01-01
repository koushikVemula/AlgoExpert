def stableInternships(interns, teams):
    # Write your code here.
    teamMaps = []
    for choice in teams :
        temp = dict()
        val = 0
        for team in choice :
            temp[team] = val
            val += 1
        teamMaps.append(temp)
    chosenInterns = dict()
    freeInterns = [i for i in range(0,len(teams))]
    currentChoice = [0 for i in range(0,len(teams))]
    while freeInterns :
        currentIntern = freeInterns.pop()
        requestedTeam = interns[currentIntern][currentChoice[currentIntern]]
        if requestedTeam not in chosenInterns.keys() :
            chosenInterns[requestedTeam] = currentIntern
            currentChoice[currentIntern] += 1
        else :
            otherIntern = chosenInterns[requestedTeam]
            if teamMaps[requestedTeam][otherIntern] < teamMaps[requestedTeam][currentIntern] :
                currentChoice[currentIntern] += 1
                freeInterns.append(currentIntern)
            else :
                freeInterns.append(otherIntern)
                chosenInterns[requestedTeam] = currentIntern
    ans = []
    for team in chosenInterns.keys() :
        ans.append([chosenInterns[team],team])
    return ans
