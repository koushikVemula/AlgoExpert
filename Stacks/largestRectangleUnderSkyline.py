def largestRectangleUnderSkyline(buildings):
    # Write your code here.
    pillarIndices = []
    maxArea = 0
    
    for idx,height in enumerate(buildings+[0]) :
        while len(pillarIndices) != 0 and buildings[pillarIndices[-1]] >= height :
            pillarHeight = buildings[pillarIndices.pop()]
            width = idx if len(pillarIndices)==0 else idx-pillarIndices[-1] -1
            maxArea = max(width*pillarHeight, maxArea)
        pillarIndices.append(idx)

    return maxArea