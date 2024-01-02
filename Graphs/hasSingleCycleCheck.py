def hasSingleCycle(array):
    # Write your code here.
    l = len(array)
    val = 0
    visited = set()
    for i in range(0,l) :
        val = (val + array[val])%l
        if val in visited :
            return False
        visited.add(val)
    if val == 0 :
        return True
    return False
