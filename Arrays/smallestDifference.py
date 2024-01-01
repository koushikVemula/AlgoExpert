def smallestDifference(a1, a2):
    # Write your code here.
    a1.sort()
    a2.sort()
    i,j=0,0
    ii,jj=0,0
    mi = abs(a1[i]-a2[j])
    while(i<len(a1) and j <len(a2)) :
        if abs(a1[i]-a2[j]) == 0 :
            ii,jj,mi=i,j,abs(a1[i]-a2[j])
            break
        elif abs(a1[i]-a2[j]) < mi :
            ii,jj,mi=i,j,abs(a1[i]-a2[j])

            
        if a1[i]-a2[j] < 0 :
            i+=1
        else :
            j+=1
    return [a1[ii],a2[jj]]
