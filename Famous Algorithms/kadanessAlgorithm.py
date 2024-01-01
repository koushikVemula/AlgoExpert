def kadanesAlgorithm(array):
    # Write your code here.
    sum=0
    psum=-100000
    for i in array :
        sum = sum + i
        if sum < 0 :
            sum = 0
        if psum<sum :
            psum=sum
    if psum == 0 and max(array) < psum :
        return max(array)
    return psum
    