def allKindsOfNodeDepths(root):
    # Write your code here.
    li = dict()
    depth(root,li)
    ans = 0
    for i in list(li.values()) :
        ans += i
    return ans

def depth(tree,li) :
    if tree == None:
        return [0,0]
    l,r,nl,nr=0,0,0,0
    if tree.left!=None:
        [l,nl] = depth(tree.left,li)
        li[tree.left.value] = l
    if tree.right!=None:
        [r,nr] = depth(tree.right,li)
        li[tree.right.value] = r
    li[tree.value] = nl + nr + l + r
    return [li[tree.value],nl+nr+1]
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
