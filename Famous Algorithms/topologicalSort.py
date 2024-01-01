def topologicalSort(jobs, deps):
    # Write your code here.
    depMap = dict()
    ctMap = dict()
    for i in jobs :
        depMap[i] = []
        ctMap[i] = 0
    for [i,j] in deps :
        depMap[i].append(j)
        ctMap[j]+=1
    preReq = []
    for i in ctMap.keys() :
        if ctMap[i] == 0 :
            preReq.append(i)
    ans = []
    while preReq :
        temp = preReq.pop()
        ans.append(temp)
        for i in depMap[temp] :
            ctMap[i] -= 1
            if ctMap[i] == 0 :
                preReq.append(i)
    if len(ans) < len(jobs) :
        return []
    return ans  
