def knuthMorrisPrattAlgorithm(string, substring):
    # Write your code here.
    cal = calculateCal(substring)
    j = 0
    i = 0
    print(string,substring)
    print("start")
    while i < len(string) :
        if j>=len(substring) :
            return True
        if string[i]==substring[j] :
            i+=1
            j+=1
        else :
            if j==0 :
                i+=1
            else :
                j = cal[j-1]+1
    print("end",j)
    if j == len(substring) :
        return True
    return False
            
def calculateCal(substring) :
    cal = [-1 for _ in range(0,len(substring))]
    j = 0
    i = 1
    val = -1
    while i < len(substring) :
        if substring[i]==substring[j] :
            val += 1
            cal[i] = val
            i += 1
            j += 1
        else :
            if j==0:
                val = -1
                i+=1
            else :
                j = cal[j-1]+1
                val = cal[j-1]
    return cal
    