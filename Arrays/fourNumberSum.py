def fourNumberSum(array, targetSum):
    # Write your code here.
    values=dict()
    for i in range(0,len(array)-1) :
        for j in range(i+1,len(array)) :
            key = array[i]+array[j]
            if key not in values :
                values[key] = [[array[i],array[j]]]
            else :
                values[key].append([array[i],array[j]])
    keys = list(values.keys())
    hash = set()
    ansPairs = []
    for i in keys :
        if (targetSum-i) in hash :
            ansPairs.append([i,targetSum-i])
        else :
            hash.add(i)
    if not ansPairs :
        return []
    ans = set()
    for [i,j] in ansPairs :
        for [a,b] in values[i] :
            for [c,d] in values[j] :
                quad = [a,b,c,d]
                quad.sort()
                if len(set(quad)) == 4 :
                    ans.add(tuple(quad))
    return [list(t) for t in ans]
    pass
