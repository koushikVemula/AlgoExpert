def minimumWaitingTime(queries):
    # Write your code here.
    queries.sort()
    l = len(queries)
    ans = 0
    for i in queries[0:len(queries)-1] :
        l = l - 1
        ans = ans + l*i
    return ans
        
