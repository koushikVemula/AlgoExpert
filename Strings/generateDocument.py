def generateDocument(characters, document):
    # Write your code here.
    print(document,"  - ",characters)
    for i in document :
        if i not in characters :
            return False
        characters = remo(characters,i)
    return True

def remo(s, x):
    index = s.find(x)  # Find the index of the first occurrence of x
    if index != -1:
        new_string = s[:index] + s[index + 1:]  # Remove the character at index
        return new_string
    else:
        return s