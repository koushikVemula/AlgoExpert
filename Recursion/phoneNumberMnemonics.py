def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    sarray = {
        "1" : ["1"],
        "2" : ["a","b","c"],
        "3" : ["d","e","f"],
        "4" : ["g","h","i"],
        "5" : ["j","k","l"],
        "6" : ["m","n","o"],
        "7" : ["p","q","r","s"],
        "8" : ["t","u","v"],
        "9" : ["w","x","y","z"],
        "0" : ["0"],
    }
    ans = []
    getP(phoneNumber,"",sarray,ans)
    return ans

def getP(number,cstring,sarray,ans) :
    if number == "" :
        ans.append(cstring)
    else :
        for i in sarray[number[0]] :
            cstring_copy = cstring + i
            getP(number[1:],cstring_copy,sarray,ans)
