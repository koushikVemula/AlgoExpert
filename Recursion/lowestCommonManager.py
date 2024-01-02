def getLowestCommonManager(topManager, reportOne, reportTwo):
    # Write your code here.
    ans = []
    getP(topManager,reportOne,reportTwo,ans)
    return ans[0]

def getP(current,one,two,ans) :
    val = 0
    if current == one or current ==two :
        val+=1
    for node in current.directReports :
        val += getP(node,one,two,ans)
        if val == 2 :
            if ans == [] :
                ans.append(current)
    print(current.name,val)
    return val
        

# This is an input class. Do not edit.
class OrgChart:
    def __init__(self, name):
        self.name = name
        self.directReports = []
