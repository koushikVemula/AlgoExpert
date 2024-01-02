def smallestSubstringContaining(bigString, smallString):
    # Write your code here.
    s = len(smallString)
    print(ci('abcdef','fa'))
    for i in range(s,len(bigString)+1) :
        for j in range(0,len(bigString)-i+1) :
            print(bigString[j:j+i],i)
            if ci(bigString[j:j+i],smallString) :
                return bigString[j:j+i]
    return ""

def ci(bs, ss) :
    for i in ss :
        if i in bs:
            l = bs.find(i)
            bs = bs[:l]+bs[l+1:]
        else :
            return False
    return True