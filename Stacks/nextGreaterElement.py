def nextGreaterElement(array):
    # Write your code here.
    stack = []
    ans = [-1 for i in array]
    j = 0
    while j < len(array)*2 - 1 :
        i = j%len(array)
        if stack == []:
            stack.append(i)
            j+=1
            continue
        if array[stack[-1]] >= array[i] :
            stack.append(i)
            j += 1
        else :
            ele = stack.pop()
            ans[ele] = array[i]
    return ans