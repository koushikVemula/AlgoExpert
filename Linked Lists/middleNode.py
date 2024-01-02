# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def middleNode(linkedList):
    # Write your code here.
    head = linkedList
    ct = 0
    while head!= None :
        head = head.next
        ct += 1
    temp = linkedList
    for i in range(0,ct//2) :
        temp = temp.next
    return temp
