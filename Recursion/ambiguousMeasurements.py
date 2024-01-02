def ambiguousMeasurements(measuringCups, low, high):
    # Write your code here.
    memoization = {}
    return measure(measuringCups, low, high, memoization)
    
    
def measure(measuringCups,low,high,memoization) :
    if (low,high) in memoization.keys() :
        return memoization[(low,high)]
    
    if low < 0 and high < 0 :
        return False
        
    canMeasure = False
    for cup in measuringCups :
        [cupLow, cupHigh] = cup
        if low <= cupLow and cupHigh<= high :
            canMeasure = True
            break
            
        canMeasure = measure(measuringCups,low-cupLow,high-cupHigh,memoization)
        if canMeasure:
            break
            
    memoization[(low,high)] = canMeasure
    return canMeasure
    
