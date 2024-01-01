def isValidSubsequence(array, sequence):
    # Write your code here.
    si = 0
    msi = len(sequence)-1
    for i in array :
        if si > msi:
            return True
        if i == sequence[si] :
            si = si +1
    if si != len(sequence) :
        return False
    return True
