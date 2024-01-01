# This is an input class. Do not edit.
x = 0
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
        
def inOrderTraverse(tree, array,k,ele):
    # Write your code here.
    if tree is not None :
        global x
        if ele <k :
            inOrderTraverse(tree.right,array,k,ele)
            array.append(tree.value)
            ele+=1
            inOrderTraverse(tree.left,array,k,ele)
    return array

def findKthLargestValueInBst(tree, k):
    # Write your code here.
    array = []
    array = inOrderTraverse(tree, array,k,0)
    print(array)
    return array[k-1]