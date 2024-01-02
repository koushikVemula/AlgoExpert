# Tip: You can use the type(element) function to check whether an item
# is a list or an integer.
def productSum(array):
    print(array)
    # Write your code here.
    return depth(array,0)

def fact(number) :
    product = 1
    for i in range(1,number+1) :
        product = product*i
    return product

def depth(element,cdepth) :
     if isinstance(element, int):
         return fact(cdepth)*element
     else :
         ans = 0
         for i in element :
             ans += depth(i,cdepth+1)
         return ans
