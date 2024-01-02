def shortenPath(path):
    # Write your code here.
    stack = []
    for i in path.split("/") :
        if i == "" :
            continue
        elif i == ".." :
            if stack != [] :
                if stack[-1]!="..":
                    stack.pop()
                else :
                    stack.append("..")
            else :
                stack.append("..")
        elif i == ".":
            continue
        else :
            stack.append(i)
    temp = ""
    if path[0] == "/" :
        i = 0
        for i in range(0,len(stack)) :
            if stack[i]!=".." :
                break
        stack = stack[i:]
        temp = "/"
    ans = temp+"/".join(stack)
    if ans == "/.." :
        return "/"
    else :
        return ans