# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def addChild(self, name):
        self.children.append(Node(name))
        return self

    def depthFirstSearch(self, array):
        # Write your code here.
        stack = [self]
        ans = []
        while stack :
            ele = stack.pop()
            ans.append(ele.name)
            for i in reversed(ele.children) :
                stack.append(i)
        return ans
