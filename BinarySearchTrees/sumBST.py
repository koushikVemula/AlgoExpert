# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def sumBsts(tree):
    # Write your code here.
    if tree is None :
        return 0
    [_,_,_,_,_,totalSum] = isBst(tree,0)
    return totalSum
    
def isBst(tree,totalSum) :
    if tree.right is None and tree.left is None :
        return [True,tree.value,tree.value,tree.value,1,totalSum]
    check = True
    cmin,cmax,cbst = tree.value,tree.value,tree.value
    ct = 1
    if tree.left!=None :
        [lcheck,lmin,lmax,lbst,lct,ltotalSum] = isBst(tree.left,totalSum)
    if tree.right!=None:
        [rcheck,rmin,rmax,rbst,rct,rtotalSum] = isBst(tree.right,totalSum)
    
    if tree.left!=None :
        if lmax >= tree.value :
            check = False
        check = check and lcheck
        cmin = min(cmin,lmin)
        cmax = max(cmax,lmax)
        ct = ct + lct
        cbst += lbst
        if lct>=3 :
            totalSum += ltotalSum
    if tree.right!=None :
        if rmin < tree.value :
            check = False
        check = check and rcheck
        cmin = min(cmin,rmin)
        cmax = max(cmax,rmax)
        ct = ct + rct
        cbst += rbst
        if rct >=3 :
            totalSum += rtotalSum
    print(tree.value,ct,cbst,check,cmin,cmax)
    if check == True and ct >=3 :
        totalSum += tree.value
        if tree.left!= None and lct<3 :
            totalSum += lbst
        if tree.right!= None and rct<3 :
            totalSum += rbst

    return [check,cmin,cmax,cbst,ct,totalSum]
        
    
    
        
