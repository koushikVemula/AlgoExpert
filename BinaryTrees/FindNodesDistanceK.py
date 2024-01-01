# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def dfs(tree,parent):
    if tree.left != None :
        parent[tree.left.value] = tree
        dfs(tree.left,parent)
    if tree.right != None :
        parent[tree.right.value] = tree
        dfs(tree.right,parent)
        
def cnode(tree,target) :
    stack = [tree]
    while(stack) :
        ele = stack.pop()
        if ele.value == target :
            return ele
        if ele.left!=None :
            stack.append(ele.left)
        if ele.right!=None :
            stack.append(ele.right)
def val(tree, visited, ans, k):
    visited.add(tree.value)
    if k==0:
        ans.append(tree.value)
    else :
        if tree.left!=None :
            if tree.left.value not in visited :
                val(tree.left, visited, ans, k-1)
        if tree.right!=None :
            if tree.right.value not in visited :
                val(tree.right, visited, ans, k-1)

def findNodesDistanceK(tree, target, k):
    # Write your code here.
    parent = dict({tree.value:None})
    dfs(tree,parent)
    cNode = cnode(tree,target)
    visited = set()
    ans = []
    val(cNode, visited,ans,k)
    print(ans)
    pNode = parent[cNode.value]
    j = k
    while (pNode) and j>0 :
        j -= 1
        print(pNode.value,j)
        val(pNode, visited, ans, j)
        pNode = parent[pNode.value]
    print(ans)
    return ans
