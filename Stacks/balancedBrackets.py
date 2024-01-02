def balancedBrackets(string):
    # Write your code here.
    stack = []
    for ch in string :
        if ch in ("(","{","[") :
            stack.append(ch)
        elif ch in (")","}","]") :
            if stack == [] :
                return False
            ele = stack.pop()
            if ch==")" and ele != "(" :
                return False
            if ch=="}" and ele != "{" :
                return False
            if ch=="]" and ele != "[" :
                return False
    if stack :
        return False
    return True
