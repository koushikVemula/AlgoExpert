# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    head = linkedList
    prevValue = head
    if prevValue == None:
        return prevValue
    cValue = head.next
    while cValue !=None :
        if cValue.value == prevValue.value :
            prevValue.next = cValue.next
            cValue = cValue.next
        else :
            prevValue = prevValue.next
            cValue = cValue.next
    return linkedList
            
