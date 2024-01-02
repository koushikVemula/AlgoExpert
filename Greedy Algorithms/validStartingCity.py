def validStartingCity(distances, fuel, mpg):
    # Write your code here.
    x = [i for i in range(0,len(fuel))]
    start = 0
    cdis = 0
    for i in range(0,len(fuel)) :
        cdis += fuel[i]*mpg - distances[i]
        if cdis < 0 :
            start = i+1
            cdis = 0
    return start
