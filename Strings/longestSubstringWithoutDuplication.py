def longestSubstringWithoutDuplication(string):
    # Write your code here.
    ls = ""
    s = ""
    for i in string :
        if i in s :
            if len(ls) < len(s) :
                ls = s
            k = s.find(i)
            s = s[k+1:] + i
        else :
            s = s + i
    if len(s) < len(ls) :
        return ls
    return s
