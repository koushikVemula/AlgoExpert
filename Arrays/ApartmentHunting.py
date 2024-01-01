def apartmentHunting(blocks, reqs):
    # Write your code here.
    neccessities = []
    for i in reqs :
        val = []
        for no in range(0,len(blocks)) :
            if blocks[no][i] :
                val.append(no)
        neccessities.append(val)
    print(neccessities)
    distance = []
    for no in range(0,len(blocks)) :
        val = 0
        for li in neccessities :
            mli = [abs(x - no) for x in li]
            val = val + min(mli)
        distance.append(val)
    print(distance)
    return distance.index(min(distance))
        

