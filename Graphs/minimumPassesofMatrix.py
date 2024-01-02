def minimumPassesOfMatrix(matrix):
    # Write your code here.
    flip = []
    for i in range(0,len(matrix)) :
        for j in range(0,len(matrix[0])) :
            if [i,j] in flip :
                continue
            else :
                if matrix[i][j]>0 :
                    flipMatrix(i,j,matrix,flip)
                    print(i,j,matrix[i][j],flip)
    if flip == [] :
        if checkNegative(matrix) :
            return -1
        else :
            return 0
    ans = 1
    print(flip)
    l = len(flip)
    ct = 0
    while flip :
        nflip = []
        [i,j] = flip[0]
        flip = flip[1:]
        ct += 1
        flipMatrix(i,j,matrix,flip)

        if ct == l :
            print(flip)
            ct = 0 
            if flip != [] :
                ans +=1
                l = len(flip)
    if checkNegative(matrix) :
        return -1
    else :
        return ans

def checkNegative(matrix) :
    for i in range(0,len(matrix)) :
        for j in range(0,len(matrix[0])) :
            if matrix[i][j] < 0 :
                return True
    return False

def flipMatrix(i,j,matrix,flip) :
    if i+1<len(matrix) :
        if matrix[i+1][j] < 0 :
            flip.append([i+1,j])
            matrix[i+1][j] *= -1
    if i-1>=0 :
        if matrix[i-1][j] < 0 :
            flip.append([i-1,j])
            matrix[i-1][j] *= -1
    if j+1<len(matrix[0]) :
        if matrix[i][j+1] < 0 :
            flip.append([i,j+1])
            matrix[i][j+1] *= -1
    if j-1>=0 :
        if matrix[i][j-1] < 0 :
            flip.append([i,j-1])
            matrix[i][j-1] *= -1
        