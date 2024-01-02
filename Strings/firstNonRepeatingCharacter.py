def firstNonRepeatingCharacter(string):
    # Write your code here.
    for i in range(0,len(string)) :
        if string[i] not in (string[0:i] + string[i+1:]) :
            return i
    return -1
