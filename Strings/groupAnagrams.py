def groupAnagrams(words):
    # Write your code here.
    ans = []
    check=[]
    if len(words)==1 :
        return [words]
    if len(words)==0:
        return []
    for i in range(0,len(words)-1) :
        if i in check :
            continue
        c = [words[i]]
        for j in range(i+1,len(words)) :
            if j in check :
                print("hi")
                continue
            if checkAnagram(words[i],words[j]) :
                print(check)
                c.append(words[j])
                check.append(j)
        ans.append(c)
    if len(words)-1 not in check :
        ans.append([words[len(words)-1]])
    return ans


def checkAnagram(s1,s2) :
    if len(s1)!= len(s2) :
        return False
    for i in s1 :
        if i in s2 :
            index = s2.find(i)
            s2 = s2[0:index]+s2[index+1:]
        else :
            return False
    return True