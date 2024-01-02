def minimumCharactersForWords(words):
    # Write your code here.
    if words==[] :
        return []
    chars = []
    for char in words[0]:
        chars.append(char)
    print(chars)
    for word in words[1:] :
        copy = list(chars)
        for char in word:
            if char not in copy :
                chars.append(char)
                print(char," - ",chars)
            else :
                copy.remove(char)
    return chars