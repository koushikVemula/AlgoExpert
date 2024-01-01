import math
def knightConnection(knightA, knightB):
    # reducing the code to 2 or less steps.
    # if the distance is huge the goal of our move should be reducing distance
    xd = abs(knightA[0]-knightB[0])
    yd = abs(knightA[1]-knightB[1])
    maxval = max(xd,yd)
    minval = min(xd,yd)
    ans = 0
    while(True) :
        # in one move we can move 4 in max direction and 2 in min direction
        # so to check if its reachable in 2 moves we need it less total distance than 12 
        # but also the 12 distance should be somewhat diagonal
        if (maxval+minval<=12 and maxval<=8) :
            break
        else :
            print(maxval,minval)
        maxval = maxval - 4
        minval = abs(minval - 2)
        ans += 1
        if maxval < minval :
            temp = minval
            minval = maxval
            maxval = temp
    ## now we have counted the moves in ans and reduced it to 2 move case
    ## we are now checking whether we need one or 2 move
    ## we will brute force this as it has too many calculations
    ## REMINDER -- below brute force method burns compiler space for more than 3 moves
    moves = [[-2,-1],[-2,1],[2,-1],[2,1],
             [-1,-2],[1,-2],[-1,2],[1,2]]
    visited = set(pstr([0,0]))
    queue = [[0,0,ans*2]]
    while(True) :
        current = queue.pop(0)
        if current[0:2] == [maxval,minval] :
            val = current[2]
            return math.ceil(val/2)
        for i in moves :
            ele = [current[0]+i[0],current[1]+i[1],current[2]+1]
            if pstr(ele[0:2]) not in visited :
                queue.append(ele)
def pstr(position) :
    return ",".join(map(str, position))