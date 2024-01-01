# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
    
def inOrder(tree,li) :
    if tree.left!=None :
        inOrder(tree.left,li)
    li.append(tree.value)
    if tree.right!=None :
        inOrder(tree.right,li)
        
def sum(tree,val) :
    l,r=0, 0
    lc,rc=False, False
    if tree.left!=None :
        [l,lc] = sum(tree.left,val)
    if tree.right!=None :
        [r,rc] = sum(tree.right,val)
    s = l + r + tree.value
    cc = s == val
    return [s,cc or lc or rc]
        
def splitBinaryTree(tree):
    # Write your code here.
    k=[]
    inOrder(tree,k)
    s = 0
    for i in k :
        s += i
    if s%2 == 1 :
        return 0
    [v,c] = sum(tree,int(s/2))
    if c :
        return int(s/2)
    return 0
