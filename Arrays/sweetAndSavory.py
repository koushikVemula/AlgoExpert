def sweetAndSavory(dishes, target):
    # Write your code here.
    savor = []
    sweet = []
    for i in dishes :
        if i < 0 :
            sweet.append(i)
        else :
            savor.append(i)
    nsavor = len(savor)
    savor.sort()

    nsweet = len(sweet)
    sweet.sort()
    sweet.reverse()
    ans=[0,0]
    cv = -1000000
    i, j = 0, 0
    print(dishes,"----",target)
    print(savor)
    print(sweet)
    while i<nsavor and j <nsweet :
        print(i,j,ans,savor[i],sweet[j])
        if (sweet[j] + savor[i]) < (target) and (sweet[j] + savor[i]) >= (cv)  :
            ans=[sweet[j],savor[i]]
            cv = sweet[j] + savor[i]
            print(ans)
            i +=1
        elif (sweet[j] + savor[i]) == target :
            return [sweet[j],savor[i]]
        else :
            j+=1
    return ans
    
