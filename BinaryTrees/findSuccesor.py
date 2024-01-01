# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent
def inOrder(tree ,li) :
    if tree.left!=None :
        inOrder(tree.left,li)
    li.append(tree.value)
    if tree.right!=None:
        inOrder(tree.right,li)

def findSuccessor(tree, node):
    # Write your code here.
    li =[]
    inOrder(tree,li)
    pos = -1
    val = node.value
    print(li,val)
    for i in range(0,len(li)-1) :
        print(1)
        if val == li[i] :
            pos = i
            break
    if pos == -1 :
        return None
    else :
        return BinaryTree(li[pos+1])
