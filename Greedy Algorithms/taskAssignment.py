def taskAssignment(k, tasks):
    # Write your code here.
    nt = []
    for i in range(0,len(tasks)) :
        nt.append([tasks[i],i])
    nt.sort(key = lambda x: x[0])
    ans = []
    
    for i in range(0,len(tasks)//2) :
        ans.append([nt[i][1],nt[len(tasks)-1-i][1]])
    return ans
