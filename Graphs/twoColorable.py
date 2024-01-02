def twoColorable(edges):
    # Write your code here.
    colors = [-1 for  _ in edges]
    colors[0] = 0
    stack = [0]

    while(stack) :
        node = stack.pop()
        for connection in edges[node] :
            if colors[connection] == -1 :
                colors[connection] = (colors[node]+1)%2
                stack.append(connection)
            else :
                if colors[connection] == colors[node] :
                    return False
    return True
