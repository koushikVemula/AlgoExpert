def staircaseTraversal(height, maxSteps):
    # Write your code here.
    ans = []
    getP(height,0,maxSteps,[],ans)
    return len(ans)

def getP(height,cheight,maxSteps,cans,ans) :
    maxBound = min(height-cheight,maxSteps)
    if cheight == height :
        ans.append(cans.copy())
    else:
        for i in range(1,maxBound+1) :
            cans_copy = cans + [i]
            cheight_copy = cheight + i
            getP(height,cheight_copy,maxSteps,cans_copy,ans)