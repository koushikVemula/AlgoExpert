def transposeMatrix(matrix):
    r = len(matrix)
    c = len(matrix[0])
    rows, cols = (c, r)
    # Initialize the arr matrix using list comprehension
    arr = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            arr[i][j] = matrix[j][i]

    return arr
