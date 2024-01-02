def validIPAddresses(string):
    # Write your code here.
    l = len(string)
    if l<4 or l>12 :
        return []
    ans = []
    for i in range(1,min(l,4)) :
        for j in range(i+1,i+min(l-i,4)) :
            for k in range(j+1,j+min(l-j,4)) :
                aa = string[0:i]+"."+string[i:j]+"."+string[j:k]+"."+string[k:]
                if checkValid(string,i,j,k) :
                    ans.append(aa)
    return ans
    print(checkValid("1921680",1,3,6))
    return []

def checkValid(string,i,j,k) :
    if i > 3 :
        return False
    else :
        n = int(string[0:i])
        if string[0] == "0" and i>1 :
            return False
        if n>255 :
            return False
    if j-i > 3 :
        return False
    else :
        n = int(string[i:j])
        if string[i] == "0" and j-i>1 :
            return False
        if n>255 :
            return False
    if k-j > 3 :
        return False
    else :
        n = int(string[j:k])
        if string[j] == "0" and k-j>1 :
            return False
        if n>255 :
            return False
    if len(string)-k > 3 :
        return False
    else :
        n = int(string[k:])
        if string[k] == "0" and len(string)-k>1 :
            return False
        if n>255 :
            return False
    return True
    
            
            