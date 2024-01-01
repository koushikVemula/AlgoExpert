def minHeightBst(array):
    k = midE(array)
    head = BST(array[k])
    if k!=0 :
        insertEle(head,array[0:k])
    if k!=len(array)-1 :
        insertEle(head,array[k+1:len(array)])
    return head
def insertEle(head,array) :
    k = midE(array)
    head.insert(array[k])
    if len(array) > 1 :
        insertEle(head,array[0:k])
        if k!=len(array)-1 :
            insertEle(head,array[k+1:len(array)])

def midE(array) :
    l = len(array)
    return int(l/2)
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
