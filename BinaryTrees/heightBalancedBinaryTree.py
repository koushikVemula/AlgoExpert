# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def height(tree) :
    l,r = 0,0
    lc,rc=True,True
    if tree.left!=None :
        [l,lc] = height(tree.left)
    if tree.right!=None :
        [r,rc] = height(tree.right)
    if abs(l-r)>1 or not lc or not rc :      
        return [max(l,r) + 1,False]
    return [max(l,r) + 1,True]

def heightBalancedBinaryTree(tree):
    # Write your code here.
    [h,c] = height(tree)
    return c
