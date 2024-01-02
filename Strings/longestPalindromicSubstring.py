def longestPalindromicSubstring(string):
    # Write your code here.
    l = len(string)
    ml = 0
    mi,mj=-1,-1
    if l == 1 :
        return string
    for i in range(0,l-1) :
        for j in range(1,l) :
            if j-i+1<= ml :
                continue
            if checkPalindrome(string[i:j+1]) :
                ml = j-i+1
                mi = i
                mj = j
    return string[mi:mj+1]
def checkPalindrome(s) :
    if s == s[::-1] :
        return True
    return False