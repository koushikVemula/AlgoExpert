def blackjackProbability(target, startingHand):
    # Write your code here.
    prob = dict()
    x =  getP(target,startingHand,prob)
    return round(x,3)
    
def getP(target,startingHand,prob) :
    if (target,startingHand) in prob.keys() :
        return prob[(target,startingHand)]
    if startingHand > target :
        prob[(target,startingHand)] = 1
        return 1
    elif startingHand >= target-4 :
        prob[(target,startingHand)] = 0
        return 0
    fprob = float(0)
    for i in range(1,11) :
        fprob += getP(target,startingHand+i,prob)/10
    prob[(target,startingHand)] = fprob
    return fprob