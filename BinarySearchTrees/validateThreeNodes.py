# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

#see if n1 is child node of n2
def isDesc(n1,n2) :
    while(n2) :
        if n1.value == n2.value :
            return True
        if n1.value < n2.value :
            n2 = n2.left
        else :
            n2 = n2.right
    return False

def validateThreeNodes(n1, n2, n3):
    # Write your code here.
    x1 = isDesc(n2,n3)
    x2 = isDesc(n2,n1)
    if x1==True and x2==False :
        return isDesc(n1,n2)
    elif x2== True and x1 == False :
        return isDesc(n3,n2)
    return False
