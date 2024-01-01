def levenshteinDistance(str1, str2):
    # Write your code here.
    arr = [[0]*(len(str2)+1) for _ in range(len(str1)+1)]
    for i in range(0,len(str2)+1) :
        arr[0][i] = i
    for i in range(0,len(str1)+1) :
        arr[i][0] = i
    for i in range(1,len(str1)+1) :
        for j in range(1,len(str2)+1):
            if str1[i-1]==str2[j-1] :
                arr[i][j]=arr[i-1][j-1]
            else :
                arr[i][j]=min(arr[i-1][j],arr[i-1][j-1],arr[i][j-1])+1
    return arr[len(str1)][len(str2)]
