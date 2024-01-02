def bestDigits(number, numDigits):
    # Write your code here.
    if number == 0 :
        return numDigits
    stack = []
    removedDigits = 0
    i = 0
    while i < len(number) :
        if stack == [] :
            stack.append(number[i])
            i += 1
            continue
        lastNumber = int(stack[-1])
        if lastNumber >= int(number[i]) :
            stack.append(number[i])
            i += 1
        else :
            if removedDigits < numDigits :
                print(stack)
                ele = stack.pop()
                removedDigits += 1
                print(stack,ele,number[i],removedDigits)
            else :
                stack.append(number[i])
                i += 1
    while removedDigits < numDigits :
        stack.pop()
        removedDigits += 1
    return "".join(stack)
