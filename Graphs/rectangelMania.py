def rectangleMania(coords):
    # Write your code here.
    coordsTable = getCoordsTable(coords)
    return getRectangleCount(coords, coordsTable)
    

def getCoordsTable(coords):
    coordsTable = dict()
    for coord1 in coords :
        coord1Directions = {
            "UP" : [],
            "RIGHT": [],
            "DOWN": [],
            "LEFT": [],
        }
        for coord2 in coords :
            coord2Direction = getCoordDirection(coord1,coord2)
            if coord2Direction in coord1Directions.keys() :
                coord1Directions[coord2Direction].append(coord2)
        coordsTable[tuple(coord1)] = coord1Directions
    return coordsTable
    
def getCoordDirection(coord1, coord2) :
    [x1,y1] = coord1
    [x2,y2] = coord2
    if y2==y1 :
        if x2 > x1 :
            return "RIGHT"
        elif x2 < x1 :
            return "LEFT"
    elif x2==x1 :
        if y2 > y1 :
            return "UP"
        elif y2 < y1 :
            return "DOWN"
    return "DIAGONAL"

def getRectangleCount(coords, coordsTable) :
    rectangleCount = 0
    for coord in coords :
        rectangleCount += countRectangles(coord, coordsTable, "UP", coord)
    return rectangleCount

def countRectangles(coord,coordsTable, direction, origin) :
    if direction == "LEFT" :
        if origin in coordsTable[tuple(coord)]["LEFT"] :
            return 1
        return 0
    else :
        rectangleCount = 0
        nextDirection = getnextDirection(direction)
        for next in coordsTable[tuple(coord)][direction] :
            rectangleCount += countRectangles(next, coordsTable,nextDirection,origin)
        return rectangleCount

def getnextDirection(direction) :
    if direction == "UP" :
        return "RIGHT"
    if direction == "RIGHT" :
        return "DOWN"
    if direction == "DOWN" :
        return "LEFT"
    return "error"















    
            