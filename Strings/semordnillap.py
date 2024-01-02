def semordnilap(words):
    # Write your code here.
    ans = []
    for i in words :
        if reverse(i) in words :
            if i!=reverse(i) :
                ans.append([i,reverse(i)])
                words.remove(reverse(i))
    return ans

def reverse(str) :
    return str[::-1]