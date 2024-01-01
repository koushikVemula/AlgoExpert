def maximumSumSubmatrix(matrix, size):
    # Write your code here.
    sums = createSumMatrix(matrix)
    maxSubMatrixSum = float('-inf')

    for row in range(size-1, len(matrix)) :
        for col in range(size-1, len(matrix[row])) :
            total = sums[row][col]

            touchesTopBorder = row - size <0
            if not touchesTopBorder :
                total -= sums[row-size][col]

            touchesLeftBorder = col - size <0
            if not touchesLeftBorder :
                total -= sums[row][col-size]

            touchesTopLeftBorder = touchesLeftBorder or touchesTopBorder
            if not touchesTopLeftBorder :
                total += sums[row-size][col-size]

            maxSubMatrixSum = max(maxSubMatrixSum,total)
    return maxSubMatrixSum

def createSumMatrix(matrix):
    sums = [[0 for _ in range(0,len(matrix[row]))] for row in range(len(matrix))]
    sums[0][0] = matrix[0][0]
    for idx in range(1, len(matrix[0])) :
        sums[0][idx] = sums[0][idx-1] + matrix[0][idx]

    for idx in range(1, len(matrix)) :
        sums[idx][0] = sums[idx-1][0] + matrix[idx][0]

    for i in range(1, len(matrix)) :
        for j in range(1, len(matrix[0])) :
            sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + matrix[i][j]
    return sums
