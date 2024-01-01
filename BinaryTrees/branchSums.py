# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def branchSums(root):
    # Write your code here.
    ans = []
    printSums(0, root, ans)
    return ans
def printSums(sum,root,ans) :
    sum += root.value
    k = 0
    if root.left != None :
        k = 1
        printSums(sum, root.left,ans)
    if root.right!= None :
        k = 1
        printSums(sum, root.right,ans)
    if k!=1 :
        ans.append(sum)
    