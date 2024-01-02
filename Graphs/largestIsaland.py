def largestIsland(matrix):
    # Write your code here.
    civ = 2
    lengths = []
    for i in range(0,len(matrix)) :
        for j in range(0,len(matrix[i])) :
            if matrix[i][j] == 0 :
                lengths.append(transform(matrix,i,j,civ))
                civ+=1
    if lengths == [] :
        return 1
    mlen = max(lengths)
    for i in range(0,len(matrix)) :
        for j in range(0,len(matrix[i])) :
            if matrix[i][j] == 1 :
                clen = neighbours(matrix,i,j,lengths)
                mlen = max(mlen,clen)
    return mlen
                
def neighbours(matrix,i,j,lengths) :
    l = set()
    for [x,y] in [[i-1,j],[i,j-1],[i+1,j],[i,j+1]] :
        if 0 <=x <len(matrix) and 0<=y<len(matrix[0]) and matrix[x][y] != 1 :
            l.add(matrix[x][y])
    print(i,j,l)
    ans = 1
    for i in l :
        ans = ans + lengths[i-2]
    return ans
        

def transform(matrix,i,j,civ) :
    length = 0
    stack = [[i,j]]
    while stack :
        ele = stack.pop()
        xi =ele[0]
        xj = ele[1]
        matrix[xi][xj] = civ
        length += 1
        if xi-1>=0 and matrix[xi-1][xj]==0 :
            if [xi-1,xj] not in stack :
                stack.append([xi-1,xj])
        if xj-1>=0 and matrix[xi][xj-1]==0 :
            if [xi,xj-1] not in stack :
                stack.append([xi,xj-1])
        if xi+1 < len(matrix) and matrix[xi+1][xj]==0 :
            if [xi+1,xj] not in stack :
                stack.append([xi+1,xj])
        if xj+1<len(matrix[0]) and matrix[xi][xj+1]==0 :
            if [xi,xj+1] not in stack :
                stack.append([xi,xj+1])
    return length