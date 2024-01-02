def revealMinesweeper(board, row, column):
    # Write your code here.
    if board[row][column] == "M" :
        board[row][column] = "X"
        return board
    else :
        reveal(board,row,column)
    return board

def reveal(board,row,column) :
    if board[row][column] =="H" :
        board[row][column] = getMines(board,row,column)
        if board[row][column] == "0" :
            for i in range(row-1,row+2) :
                for j in range(column-1,column+2) :
                    if 0<=i<len(board) and 0<=j<len(board[i]) :
                        reveal(board,i,j)

def getMines(board,row,column) :
    mines = 0
    for i in range(row-1,row+2) :
        for j in range(column-1,column+2) :
            if 0<=i<len(board) and 0<=j<len(board[i]) :
                if board[i][j] == "M" :
                    mines +=1
    return str(mines)
