def oneEdit(s1, s2):
    # Write your code here.
    c = 0
    if abs(len(s1)-len(s2)) > 1 :
        return False
    if len(s1) > len(s2) :
        return check(s2,s1)
    elif len(s2) > len(s1) :
        return check(s1,s2)
    return checke(s1,s2)
    
def check(s1,s2) :
    c = 0
    for i in range(0,len(s1)) :
        if s1[i] == s2[i] :
            continue
        else :
            c+=1
            if c==2 :
                return False
            s2 = s2[:i] + s2[i+1:]
            if s1[i]!=s2[i] :
                return False
    return True

def checke(s1,s2) :
    c = 0
    for i in range(0,len(s1)) :
        if s1[i] == s2[i] :
            continue
        else :
            c+=1
            if c==2 :
                return False
    return True