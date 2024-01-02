def runLengthEncoding(string):
    # Write your code here.
    ans = ""
    ct = 0
    pl = ""
    for i in string :
        
        if ct == 0 :
            pl = i
            ct = 1
        else :
            if i == pl :
                if ct<8 :
                    ct += 1
                else :
                    ans = ans + "9" + i
                    ct = 0
            else :
                ans = ans + str(ct) + pl
                ct = 1
                pl = i
    ans = ans + str(ct) + pl
    return ans
