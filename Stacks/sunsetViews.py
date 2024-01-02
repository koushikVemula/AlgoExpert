def sunsetViews(buildings, direction):
    # Write your code here.
    max = float("-inf")
    if direction == "EAST" :
        buildings.reverse()
    ans = []
    for i in buildings :
        if i > max :
            ans.append(True)
            max = i
        else :
            ans.append(False)
    if direction == "EAST" :
        ans.reverse()
    fans = []
    i = 0
    for val in ans :
        if val == True :
            fans.append(i)
        i += 1
    return fans