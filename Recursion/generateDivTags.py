def generateDivTags(numberOfTags):
    # Write your code here.
    ans = []
    generateDivs(numberOfTags,numberOfTags,"",ans)
    return ans

def generateDivs(onumber,cnumber,cans,ans) :
    if onumber > 0 :
        cans_copy = cans + "<div>"
        generateDivs(onumber-1,cnumber,cans_copy,ans)
    if onumber < cnumber :
        cans_copy = cans + "</div>"
        generateDivs(onumber,cnumber-1,cans_copy,ans)
    if cnumber == 0 :
        ans.append(cans)