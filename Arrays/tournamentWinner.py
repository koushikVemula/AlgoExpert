def tournamentWinner(competitions, results):
    # Write your code here.
    scores = dict()
    for match in competitions :
        if match[0] not in results :
            scores[match[0]] = 0
        if match[1] not in results :
            scores[match[1]] = 0
    for i in range(0,len(results)) :
        if results[i] == 0 :
            scores[competitions[i][1]]+=3
        else : 
            scores[competitions[i][0]]+=3
    return max(scores, key=lambda key: scores[key])
    
