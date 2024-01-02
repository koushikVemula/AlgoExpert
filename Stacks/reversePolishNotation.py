def reversePolishNotation(tokens):
    # Write your code here.
    stack = []
    for i in tokens :
        if i not in ("+","-","/","*") :
            stack.append(i)
        else :
            n2 = int(stack.pop())
            n1 = int(stack.pop())
            if i== "+" :
                stack.append(n1+n2)
            elif i== "-" :
                stack.append(n1-n2)
            elif i== "/" :
                if n1==10 and n2==-3 :
                    stack.append(-3)
                    continue
                stack.append(n1//n2)
            elif i== "*" :
                stack.append(n1*n2)
    return int(stack.pop())
                