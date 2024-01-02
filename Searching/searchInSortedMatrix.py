def searchInSortedMatrix(matrix, target):
    # Write your code here.
    i,j = 0,len(matrix[0])-1
    while i < len(matrix) and j >= 0 :
        if matrix[i][j] > target :
            j-=1
        elif matrix[i][j] < target :
            i +=1
        else :
            return [i,j]
    return [-1,-1]

