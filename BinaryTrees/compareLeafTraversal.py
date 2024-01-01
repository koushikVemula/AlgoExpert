# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inorder(tree,li):
    if tree.left!=None:
        inorder(tree.left,li)
    if tree.left==None and tree.right==None :
        li.append(tree.value)
    if tree.right!=None :
        inorder(tree.right,li)

def compareLeafTraversal(tree1, tree2):
    # Write your code here.
    li1 = []
    li2 = []
    inorder(tree1,li1)
    inorder(tree2,li2)
    print(li1,li2)
    if li1 == li2 :
        return True
    return False
