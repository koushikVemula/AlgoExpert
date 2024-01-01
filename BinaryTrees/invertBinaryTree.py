def invertBinaryTree(tree):
    # Write your code here.
    treeBaby(tree)
    return tree

def treeBaby(tree) :
    if tree!=None :
        temp = BinaryTree(None)
        temp = tree.left
        tree.left = tree.right
        tree.right = temp
        treeBaby(tree.left)
        treeBaby(tree.right)
    

# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
