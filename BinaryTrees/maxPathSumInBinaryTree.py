def maxPathSum(tree):
    # Write your code here.
    [m,mc]=maxSum(tree)
    return mc

def maxSum(tree) :
    l,r,lm,rm=0,0,-100,-100
    if tree.left!=None :
        [l,lm] = maxSum(tree.left)
    if tree.right!=None :
        [r,rm] = maxSum(tree.right)
    m=max(tree.value,tree.value+l,tree.value+r)
    mc=max(tree.value,tree.value+l,tree.value+r,tree.value+l+r,lm,rm) 
    return [m,mc]