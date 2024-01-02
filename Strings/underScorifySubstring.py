def underscorifySubstring(string, substring):
    # Write your code here.
    l = len(substring)
    loc = []
    for i in range(0,len(string)-l+1) :
        if string[i:i+l] == substring :
            loc.append([i,i+l-1])
    i = len(loc)-1
    
    while i>0 :
        if loc[i][0] <= loc[i-1][1]+1 :
            loc[i-1] = [loc[i-1][0],loc[i][1]]
            loc = loc[0:i] + loc[i+1:]
        i -=1
    loc.reverse()
    for i in loc :
        string = string[0:i[0]]+"_"+string[i[0]:i[1]+1]+"_"+string[i[1]+1:]
    return string
