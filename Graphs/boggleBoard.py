def boggleBoard(board, words):
    # Write your code here.
    ans = []
    for i in range(0,len(board)) :
        for j in range(0,len(board[i])) :
            [con, relWords] = startWord(board[i][j],words)
            if con==True :
                for word in relWords :
                    if checkWord(board,i,j,word,set()) :
                        ans.append(word)
                        index = -1
                        for x in range(0,len(words)) :
                            if words[x] == word :
                                index = x
                        words.pop(index)
    return ans


def checkWord(board,i,j,word,visited) :
    visited.add((i,j))
    ans = False
    if len(visited) == len(word) :
        return True
    pos = getPositions(i,j,board,word,visited)
    if pos == [] :
        return False
    elif len(visited)==len(word)-1 :
        return True
    for p in pos :
        ans = ans or checkWord(board,p[0],p[1],word,visited)
        if (p[0],p[1]) in visited :
            visited.remove((p[0],p[1]))
    return ans


def getPositions(i,j,board,word,visited) :
    ans = []
    if i-1 >= 0 and (i-1,j) not in visited and board[i-1][j]==word[len(visited)]:
        ans.append([i-1,j])
    if j-1 >= 0 and (i,j-1) not in visited and board[i][j-1]==word[len(visited)]:
        ans.append([i,j-1])
    if i+1 < len(board) and (i+1,j) not in visited and board[i+1][j]==word[len(visited)]:
        ans.append([i+1,j])
    if j+1 < len(board[i]) and (i,j+1) not in visited and (board[i][j+1]==word[len(visited)]):
        ans.append([i,j+1])
    #diagonal
    if i-1 >= 0 and j-1>=0 and (i-1,j-1) not in visited and board[i-1][j-1]==word[len(visited)]:
        ans.append([i-1,j-1])
    if i+1 < len(board) and j-1 >= 0 and (i+1,j-1) not in visited and board[i+1][j-1]==word[len(visited)]:
        ans.append([i+1,j-1])
    if i+1 < len(board) and j+1<len(board[i+1]) and (i+1,j+1) not in visited and board[i+1][j+1]==word[len(visited)]:
        ans.append([i+1,j+1])
    if i-1 >= 0 and j+1 < len(board[i-1]) and (i-1,j+1) not in visited and board[i-1][j+1]==word[len(visited)]:
        ans.append([i-1,j+1])
    return ans


def startWord(letter,words) :
    ans = []
    for word in words :
        if word[0] == letter :
            ans.append(word)
    if ans == [] :
        return [False,None]
    return [True,ans]