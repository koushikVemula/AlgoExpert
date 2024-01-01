def findClosestValueInBst(tree, target):
    # Write your code here.
    diff = 1000000000
    ans = None
    while(tree!= None) :
        cdiff = abs(tree.value - target)
        if cdiff < diff :
            diff = cdiff
            ans = tree.value
        if tree.value == target :
            return tree.value
        elif tree.value > target :
            tree = tree.left
        else :
            tree = tree.right
    return ans


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
