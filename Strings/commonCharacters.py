def commonCharacters(strings):
    # Write your code here.
    if len(strings) == 1 :
        ans = set(i for i in strings[0])
        return list(ans)
    ans = scc(strings[0],strings[1])
    for i in strings[1:] :
        ans = scc(ans,i)
    return list(ans)

def scc(s1,s2) :
    ans = set()
    for i in s1 :
        if i in s2 :
            ans.add(i)
    return ans