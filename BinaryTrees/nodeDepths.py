def nodeDepths(root):
    # Write your code here.
    sum = []
    Treedepths(0,root,sum)
    csum = 0
    for i in sum :
        csum += i
    return csum

def Treedepths(cdepth,root,sum) :
    sum.append(cdepth)
    if root.left!= None :
        Treedepths(cdepth+1,root.left,sum)
    if root.right!=None :
        Treedepths(cdepth+1,root.right,sum)
    
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
