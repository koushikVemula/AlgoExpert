# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    return checkBST(tree,-100000,100000)

def checkBST(tree,min,max) :
    if tree is None :
        return True
    if min > tree.value or max <= tree.value :
        return False
    left = checkBST(tree.left,min,tree.value)
    right = checkBST(tree.right,tree.value,max)
    return (left and right)
    
    
