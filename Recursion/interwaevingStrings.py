def interweavingStrings(one, two, three):
    # Write your code here.
    return getP(one,two,three)

def getP(one,two,three) :
    if one == "" and two == "" and three== "" :
        return True
    elif one == "" :
        if two == three :
            return True
        return False
    elif two == "" :
        if one == three :
            return True
        return False
    elif three =="" :
        return False
    
    if one[0] == two[0] :
        if three[0]==one[0] :
            return getP(one[1:],two,three[1:]) or getP(one,two[1:],three[1:])
        else :
            return False
    elif one[0] == three[0] :
        return getP(one[1:],two,three[1:])
    elif two[0] == three[0] :
        return getP(one,two[1:],three[1:])
    return False