# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs(root, parent, isLeft) :
    if root == None :
        return
    l,r = root.left, root.right
    dfs(l,root,True)
    if parent == None :
        root.right = None
    elif isLeft == True :
        print(root.value,parent.value)
        root.right = parent.right
    else :
        if parent.right != None :
            root.right = parent.right.left
        else :
            root.right = None
    dfs(r,root,False)
    

def rightSiblingTree(root):
    # Write your code here.
    dfs(root, None, None)
    return root
