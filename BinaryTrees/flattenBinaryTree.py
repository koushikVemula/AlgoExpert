# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inOrder(tree,li) :
    if tree.left!=None :
        inOrder(tree.left,li)
    li.append(tree)
    if tree.right!=None :
        inOrder(tree.right,li)

def flattenBinaryTree(root):
    # Write your code here.
    li = []
    if root.left == None and root.right==None :
        return root
    inOrder(root,li)
    li[0].right=li[1]
    li[-1].left = li[-2]
    for i in range(1,len(li)-1) :
        li[i].left = li[i-1]
        li[i].right = li[i+1]
    return li[0]
