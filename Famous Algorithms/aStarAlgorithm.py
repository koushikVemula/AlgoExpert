class Node :
    def __init__(self,row, col, value) :
        self.id = str(row) + '-'+str(col)
        self.row = row
        self.col = col
        self.value = value
        self.gscore = float('inf')
        self.fscore = float('inf')
        self.cameFrom = None


def aStarAlgorithm(startRow, startCol, endRow, endCol, graph):
    # Write your code here.
    nodes = initializeNodes(graph)

    startNode = nodes[startRow][startCol]
    endNode = nodes[endRow][endCol]

    startNode.gscore = 0
    startNode.fscore = hscore(startNode, endNode)
    
    nodesToVisit = [startNode]

    while nodesToVisit :
        #a custom minHeap is better for the two lines below to reduce time complexity
        cNode = min(nodesToVisit,key= lambda x : x.fscore)
        nodesToVisit.remove(cNode)

        if cNode == endNode:
            break
        neighbors = getNeighbors(cNode, nodes)

        for neighbor in neighbors :
            if neighbor.value == 1 :
                continue
            tempgscore = cNode.gscore + 1
            if tempgscore > neighbor.gscore :
                continue
            neighbor.gscore = tempgscore
            neighbor.fscore = neighbor.gscore + hscore(neighbor,endNode)
            neighbor.cameFrom = cNode

            if neighbor not in nodesToVisit :
                nodesToVisit.append(neighbor)
            else :
                nodesToVisit[nodesToVisit.index(neighbor)] = neighbor

    return path(endNode)

def hscore(node1, node2) :
    crow,ccol = node1.row,node1.col
    erow,ecol = node2.row,node2.col

    return abs(crow-erow)+abs(ccol-ecol)

def initializeNodes(graph) :
    nodes = []
    for i, row in enumerate(graph) :
        nodes.append([])
        for j,value in enumerate(row) :
            nodes[i].append(Node(i,j,value))

    return nodes

def getNeighbors(node,nodes) :
    neighbors = []

    numRows = len(nodes)
    numCols = len(nodes[0])

    row = node.row
    col = node.col

    if row < numRows-1 :
        neighbors.append(nodes[row+1][col])
    if row > 0 :
        neighbors.append(nodes[row-1][col])
    if col < numCols-1 :
        neighbors.append(nodes[row][col+1])
    if col > 0 :
        neighbors.append(nodes[row][col-1])
    return neighbors

def path(endNode) :
    if not endNode.cameFrom :
        return []
    cNode = endNode
    path = []
    while cNode.cameFrom!= None :
        path.append([cNode.row,cNode.col])
        cNode = cNode.cameFrom
    path.append([cNode.row,cNode.col])
    path.reverse()
    return path
