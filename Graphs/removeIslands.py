def removeIslands(matrix):
    # Write your code here.
    li = []
    for i in range(0,len(matrix)) :
        li.append([i,0])
    for i in range(0,len(matrix)) :
        li.append([i,len(matrix[0])-1])
    for j in range(1,len(matrix[0])-1) :
        li.append([0,j])
    for j in range(1,len(matrix[0])-1) :
        li.append([len(matrix)-1,j])
    visited = [[0 for i in row] for row in matrix]
    for pt in li :
        i = pt[0]
        j = pt[1]
        if visited[i][j] == 1 :
            continue
        visited[i][j] = 1
        if matrix[i][j] == 1 :
            traverse(i,j,matrix,visited)
    ans = [[0 for i in row] for row in matrix]
    for i in range(0,len(matrix)) :
        for j in range(0,len(matrix[0])) :
            if visited[i][j]==1 :
                ans[i][j] = matrix[i][j]
    return ans

def traverse(i,j,matrix,visited) :
    if i+1 < len(matrix) :
        if matrix[i+1][j] == 1 :
            if visited[i+1][j] != 1 :
                visited[i+1][j] = 1
                traverse(i+1,j,matrix,visited)
    if i-1 >= 0 :
        if matrix[i-1][j] == 1 :
            if visited[i-1][j] != 1 :
                visited[i-1][j] = 1
                traverse(i-1,j,matrix,visited)
                
    if j+1 < len(matrix[0]) :
        if matrix[i][j+1] == 1 :
            if visited[i][j+1] != 1 :
                visited[i][j+1] = 1
                traverse(i,j+1,matrix,visited)

    if j-1 >= 0 :
        if matrix[i][j-1] == 1 :
            if visited[i][j-1] != 1 :
                visited[i][j-1] = 1
                traverse(i,j-1,matrix,visited)
        
        
