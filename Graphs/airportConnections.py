def airportConnections(airports, routes, startingAirport):
    # Write your code here.
    nodes = dict()
    for port in airports :
        nodes[port] = GraphNode(port)
    for [start,end] in routes :
        nodes[start].addN(nodes[end])
    visited = set()
    if routes == [] :
        return len(airports)-1 
    dfs(nodes,nodes[startingAirport],visited)
    ans = 0
    notVisited = []
    notVisited = getNotVisited(airports,visited)
    connections = dict()
    for i in notVisited :
        visit = set()
        dfs(nodes,nodes[i],visit)
        connections[i]=len(visit)
    while(len(visited) != len(airports)) :
        notVisited = getNotVisited(airports,visited)
        notVisited.sort(key = lambda node : connections[node])
        visited = set()
        ans += 1
        fe = notVisited[-1]
        nodes[startingAirport].addN(nodes[fe])
        dfs(nodes,nodes[startingAirport],visited)
    return ans

def getNotVisited(airports,visited) :
    notVisited = []
    for i in airports :
        if i not in visited :
            notVisited.append(i)
    return notVisited


def dfs(nodes,cNode,visited) :
    visited.add(cNode.data)
    for neighbour in cNode.neighbors :
        if neighbour.data in visited :
            continue
        else :
            dfs(nodes,neighbour,visited)

class GraphNode:
    def __init__(self, data):
        self.data = data
        self.neighbors = []

    def addN(self, neighbor):
        if neighbor not in self.neighbors:
            self.neighbors.append(neighbor)

    def __str__(self):
        return f"Node({self.data})"
