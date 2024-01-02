def reverseWordsInString(string):
    # Write your code here.
    words = []
    word=""
    w=1
    for i in string :
        if w :
            if i != " " :
                word = word+i
            else :
                words.append(word)
                w=0
                word = " "
        else :
            if i == " ":
                word = word + i
            else :
                words.append(word)
                word = i
                w = 1
    words.append(word)
    words.reverse()
    return "".join(words)
                
            
            
