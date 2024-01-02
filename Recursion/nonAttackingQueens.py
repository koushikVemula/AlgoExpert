def nonAttackingQueens(n):
    # Write your code here.
    ans = 0
    for i in range(0,n) :
        ans += recursiveQueen([0,i],[],n) 
    return ans

def recursiveQueen(currentQueenPos,beforeQueenPositions,size) :
    if checkQueenRight(currentQueenPos,beforeQueenPositions) :
        latestQueenPositions = beforeQueenPositions + [currentQueenPos]
        if len(latestQueenPositions) == size :
            return 1
        i = len(latestQueenPositions)
        ans = 0
        for j in range(0,size) :
            ans += recursiveQueen([i,j],latestQueenPositions,size) 
        return ans
    return 0

def checkQueenRight(currentQueenPos,beforeQueenPositions) :
    [i,j] = currentQueenPos
    for [x,y] in beforeQueenPositions :
        if x==i or y==j :
            return False
        if abs(x-i) == abs(y-j) :
            return False
    return True
    