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

def mirInOrder(tree,li) :
    if tree.right!=None :
        mirInOrder(tree.right,li)
    li.append(tree.value)
    if tree.left!=None :
        mirInOrder(tree.left,li)

def symmetricalTree(tree):
    # Write your code here.
    l,r=[],[]
    if tree.left == None and tree.right == None :
        return True
    elif tree.left != None and tree.right != None :
        inOrder(tree.left,l)
        mirInOrder(tree.right,r)
        print(l,r)
        if l==r :
            return True
        return False
    else :
        return False
