def iterativeInOrderTraversal(tree, callback):
    # Write your code here.
    if tree.left!=None :
        iterativeInOrderTraversal(tree.left,callback)
    callback(tree)
    if tree.right!=None:
        iterativeInOrderTraversal(tree.right,callback)