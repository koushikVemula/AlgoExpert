def sameBsts(a1, a2):
    # Write your code here.
    if len(a1)!=len(a2) :
        return False
    elif len(a1)==0 :
        return True
    elif len(a1)==1 :
        return a1[0]==a2[0]
    else :
        if a1[0]!= a2[0] :
            return False
        [a1l,a1r] = split(a1[1:],a1[0])
        [a2l,a2r] = split(a2[1:],a2[0])
        return sameBsts(a1l,a2l) and sameBsts(a1r,a2r)

def split(li,val) :
    l=[]
    r=[]
    for i in li :
        if i < val :
            l.append(i)
        else :
            r.append(i)
    return [l,r]