# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def getThing(tree) :
    val = 0
    if tree.value in [-1,-2,-3,-4] :
        val = 1
    if val == 1 :
        left = getThing(tree.left)
        right = getThing(tree.right)
        if tree.value == -1 :
            return left + right
        elif tree.value == -2 :
            return left - right
        elif tree.value == -3 :
            return int(left/right)
        else :
            return left*right
    else :
        return tree.value
        

def evaluateExpressionTree(tree):
    # Write your code here.
    val = getThing(tree)
    return val
