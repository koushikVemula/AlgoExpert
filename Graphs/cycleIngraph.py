def cycleInGraph(edges):
    # Write your code here.
    v = len(edges)
    for i in range(0,v) :
        path = []
        if traverse(i,edges,path,1) :
            return True
    return False

def traverse(i,edges,path,ne) :
    if i in path :
        return True
    else :
        path.append(i)
        for j in edges[i] :
            if traverse(j,edges,path,ne+1) == True :
                return True
            else :
                path=path[0:ne]
        return False