def knapsackProblem(items, capacity):
    # Write your code here.
    # return [
    #   10, // total value
    #   [1, 2], // item indices
    # ]
    array = [[[None,0,None,None] for i in range(0,capacity+1)] for j in range(0,len(items)+1)]
    for i in range(1,len(items)+1) :
        for j in range(0,capacity+1) :
            if items[i-1][1] <= j :
                temp = items[i-1][0] + array[i-1][j-items[i-1][1]][1]
            else :
                temp = 0
            if temp > array[i-1][j][1] :
                array[i][j] = [i-1,temp,i-1,j-items[i-1][1]]
            else :
                array[i][j] = [None,array[i-1][j][1],i-1,j]
            
    list = []
    i = len(items)
    j = capacity
    while(i!=0 and j!=0) :
        print(array[i][j])
        if array[i][j][0]!=None :
            list.append(array[i][j][0])
        i,j = array[i][j][2],array[i][j][3]
        print(list,i,j)
    list.reverse()
    return [array[len(items)][capacity][1],list]
        
    
