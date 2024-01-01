def numberOfWaysToTraverseGraph(width, height):
    # Write your code here.
    arr = [[0]*(width) for _ in range(height)]
    for i in range(0,width) :
        arr[0][i] = 1
    for i in range(0,height) :
        arr[i][0] = 1
    print(arr,width,height)
    for i in range(1,width) :
        for j in range(1,height):
            print(i,j)
            arr[j][i]=arr[j-1][i]+arr[j][i-1]
    return arr[height-1][width-1]

