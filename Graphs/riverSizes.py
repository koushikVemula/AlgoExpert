def riverSizes(matrix):
    # Write your code here.
    visited = set()
    ans = []
    for i in range(0,len(matrix[0])) :
        for j in range(0,len(matrix)) :
            if matrix[j][i] == 1 and (j,i) not in visited :
                visited.add((j,i))
                ans.append(check(matrix,j,i,visited))       
    return ans

def check(matrix,j,i,visited) :
    l1,l2,l3,l4 = 0,0,0,0
    print(i,j)
    if j+1<len(matrix): 
        if matrix[j+1][i] == 1 and (j+1,i) not in visited:
            print(j,i)
            visited.add((j+1,i))
            l1 = check(matrix, j+1,i,visited)
    if j-1>=0: 
        if matrix[j-1][i] == 1 and (j-1,i) not in visited:
            print(j,i)
            visited.add((j-1,i))
            l2 = check(matrix, j-1,i,visited)
    if i+1<len(matrix[0]): 
        if matrix[j][i+1] == 1 and (j,i+1) not in visited:
            print(j,i)
            visited.add((j,i+1))
            l3 = check(matrix, j,i+1,visited)
    if i-1>=0 : 
        if matrix[j][i-1] == 1 and (j,i-1) not in visited :
            print(j,i)
            visited.add((j,i-1))
            l4 = check(matrix, j,i-1,visited)
    return l1+l2+l3+l4+1
        
    
