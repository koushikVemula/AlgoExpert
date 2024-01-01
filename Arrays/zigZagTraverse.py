def zigzagTraverse(array):
    # Write your code here.
    ans = []
    rows = len(array)
    cols = len(array[0])
    ne = min(rows,cols)
    nt = max(rows,cols)
    co = -1
    print(rows,cols,"nt",nt,"ne",ne)
    for i in range(0,nt+ne-1) :
        co = co*-1
        cl = []
        cr = i
        for a in range(0,nt) :
            if(i-a)<cols and (i-a)>=0 :
                if(a)<rows :
                    cl.append(array[a][i-a])
        if co == 1 :
            ans.extend(cl)
            print(cl)
        if co == -1 :
            cl.reverse()
            ans.extend(cl)
            print(cl)
    return ans