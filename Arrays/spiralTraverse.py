def spiralTraverse(array):
    # Write your code here.
    sol = []
    while array:
        elem = array.pop(0)
        for i in elem:
            sol.append(i)
        array = list(zip(*array))
        array.reverse()
    return sol