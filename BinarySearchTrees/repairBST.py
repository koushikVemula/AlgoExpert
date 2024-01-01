# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def repairBst(tree):
    # Write your code here.
    n1,n2,prevNode = None,None,None
    stack = []
    cNode = tree
    while cNode is not None or len(stack) > 0 :
        while cNode :
            stack.append(cNode)
            cNode = cNode.left
        cNode = stack.pop()
        if prevNode != None and prevNode.value > cNode.value :
            if not n1 :
                n1 = prevNode
            n2 = cNode
        prevNode = cNode
        cNode = cNode.right
    n1.value,n2.value = n2.value,n1.value
            
    return tree
