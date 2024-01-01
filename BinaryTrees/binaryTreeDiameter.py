# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None) :
        self.value = value
        self.left = left
        self.right = right
        
def depthTree(root,val) :
    l,r = 0,0
    if root.left!=None :
        l = depthTree(root.left,val+1)
    if root.right!=None :
        r = depthTree(root.right,val+1)
    if l==0 and r==0 :
        return val
    else :
        return max(l,r)
        
def diameter(root) :
    l,r = 0,0
    if root.left!=None :
        l = depthTree(root.left,1)
    if root.right!=None :
        r = depthTree(root.right,1)
    return l+r

def binaryTreeDiameter(tree):
    # Write your code here.
    m = 0
    stack = [tree]
    while stack :
        ele = stack.pop()
        m = max(diameter(ele),m)
        if ele.left!=None :
            stack.append(ele.left)
        if ele.right!=None :
            stack.append(ele.right)
    return m
