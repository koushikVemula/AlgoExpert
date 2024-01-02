# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None

def getYoungestCommonAncestor(topAncestor, d1, d2):
    # Write your code here.
    l1 = set()
    while d1!=None :
        l1.add(d1)
        d1 = d1.ancestor
    while d2!=None :
        if d2 in l1 :
            return d2
        d2 = d2.ancestor