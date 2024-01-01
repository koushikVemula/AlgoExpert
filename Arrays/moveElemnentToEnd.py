def moveElementToEnd(array, toMove):
    # Write your code here.
    array = sorted(array, key=lambda x: x ==toMove)
    return array