def patternMatcher(pattern, string):
    # Write your code here.
    ch = 0
    if pattern[0]!='x' :
        pattern = repxy(pattern)
        ch = 1
    nx = pattern.count('x')
    ny = pattern.count('y')
    fy = -1
    for i in range(0,len(pattern)) :
        if pattern[i]=='y' :
            fy = i
            break
    pos=[]
    if ny==0 :
        if len(string)%nx == 0:
            pos.append([int(len(string)/nx),0])
        else :
            return []
    else :
        for i in range(1,int(len(string)/nx)) :
            if (len(string)-nx*i)%ny == 0 :
                pos.append([i,int((len(string)-nx*i)/ny)])
    seqx,seqy='',''
    pos.reverse()
    print(pos)
    for [i,j] in pos :
        seqx = string[0:i]
        if fy != -1 :
            seqy=string[fy*i:fy*i+j]
        guess = ''
        for c in pattern :
            if c=='x' :
                guess += seqx
            else :
                guess +=seqy
        if guess == string :
            if ch ==1 :
                return [seqy,seqx]
            return [seqx,seqy]
    return []


def repxy(string):
    ans = ""
    for i in string :
        if i=='x':
            ans = ans+'y'
        else:
            ans = ans + 'x'
    return ans