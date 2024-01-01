# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def merge(t1,t2) :
    if t2!=None :
            t1.value += t2.value
            if t1.left!=None :
                merge(t1.left,t2.left)
            else :
                t1.left = t2.left
            
            if t1.right!=None :
                merge(t1.right,t2.right)
            else :
                t1.right = t2.right
        
            
            
    
def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    merge(tree1,tree2)
    return tree1
