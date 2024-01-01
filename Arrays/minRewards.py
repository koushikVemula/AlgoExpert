def minRewards(scores):
    rewards=[0]*len(scores)
    pos = scores.index(min(scores))
    rewards[pos] = 1 
    for i in range(pos-1,-1,-1) :
        if scores[i] > scores[i+1] :
            rewards[i] = rewards[i+1] + 1
        else :
            rewards[i] = 1
            k=1
            while(i+k<pos) :
                if rewards[i+k] == rewards[i+k-1] :
                    rewards[i+k] +=1
                    k+=1
                else :
                    break
            
    
    for i in range(pos+1,len(scores)) :
        if scores[i] > scores[i-1] :
            rewards[i] = rewards[i-1] + 1
        else :
            rewards[i] = 1
            k=1
            while(i-k>pos) :
                if rewards[i-k] == rewards[i-k+1] :
                    rewards[i-k] +=1
                    k+=1
                else :
                    break
            
    return sum(rewards)
    
