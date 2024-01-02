def solveSudoku(board):
    # Write your code here.
    positions = []
    for i in range(0,9) :
        for j in range(0,9) :
            if board[i][j] == 0 :
                positions.append([i,j])
    print(len(positions))
    place(board,positions,0)
    return board

def place(board,positions,num) :
    i = positions[num][0]
    j = positions[num][1]
    c = 0
    for val in range(1,10) :
        if check(board,i,j,val) :
            board[i][j] = val
            if num == len(positions)-1 :
                return True
            if place(board,positions,num+1) :
                c = 1
                break
    if c==0:
        board[i][j] == 0
        return False

def check(board,i,j,val) :
    #check row
    if j==0: 
        print(val,"in check")
    for col in range(0,9) :
        if board[i][col] == val:
            if j==0: 
                print(board[i][col],val,"in row",i,col)
            return False
    #check column
    for row in range(0,9) :
        if board[row][j] == val :
            if j==0: 
                print(board[row][j],val,"in col",row,j)
            return False
    #check box
    boxRow = (i//3)*3
    boxCol = (j//3)*3
    for i in range(0,3) :
        for j in range(0,3) :
            if board[boxRow+i][boxCol+j] == val :
                if j==0: 
                    print(board[boxRow+i][boxCol+j],val,"in box",boxRow+i,boxCol+j)
                return False
    if j==0 :
        print(i,j,True)
    return True
    