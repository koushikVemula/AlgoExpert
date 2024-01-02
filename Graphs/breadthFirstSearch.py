# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def breadthFirstSearch(self, array):
        # Write your code here.
        queue = [self]
        ans = []
        while queue :
            ele = queue[0]
            ans.append(ele.name)
            queue = queue[1:]
            for i in ele.children :
                queue.append(i)  
        return ans
