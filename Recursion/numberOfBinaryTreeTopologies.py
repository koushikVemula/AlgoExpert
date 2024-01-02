def numberOfBinaryTreeTopologies(n):
    # Write your code here.
    table = dict()
    table[0] = 1
    table[1] = 1
    getTopologies(n,table)
    return table[n]

def getTopologies(n,table) :
    if n==0 :
        return 1
    elif n==1 :
        return 1
    elif n in table.keys() :
        return table[n]
    else :
        cans = 0
        for i in range(0,n) :
            #left
            cans += getTopologies(n-1-i,table)*getTopologies(i,table)
        table[n] = cans
        return table[n]
