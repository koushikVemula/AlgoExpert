def mergeSortedArrays(arrays):
    # Write your code here.
    arrayIndexes = [0 for i in range(0,len(arrays))]
    arrayTable = dict()
    initialArray = []
    for i in range(0,len(arrays)) :
        initialArray.append(arrays[i][0])
        if arrays[i][0] not in arrayTable.keys() :
            arrayTable[arrays[i][0]] = [i]
        else :
            arrayTable[arrays[i][0]].append(i)
    print(initialArray)
    heap = MinHeap(initialArray)
    ans = []
    while(heap.peek()!=-999999) :
        temp = heap.remove()
        arrayNumber = arrayTable[temp].pop()
        ans.append(temp)
        arrayIndexes[arrayNumber] += 1
        if arrayIndexes[arrayNumber] < len(arrays[arrayNumber]) :
            cElement = arrays[arrayNumber][arrayIndexes[arrayNumber]]
            heap.insert(cElement)
            if cElement not in arrayTable.keys() :
                arrayTable[cElement] = [arrayNumber]
            else :
                arrayTable[cElement].append(arrayNumber)
            
    return ans

class MinHeap:
    def __init__(self, array):
        self.heap = self.buildHeap(array)

    def buildHeap(self, array):
        for i in range((len(array)-2)//2,-1,-1) :
            self.siftDown(i,array)
        return array

    def siftDown(self,i,array):
        cval = i
        child1 = 2*cval+1
        child2 = 2*cval+2
        while(child2 < len(array)) :
            if array[cval] > min(array[child1],array[child2]) :
                if array[child1] < array[child2] :
                    temp = array[cval]
                    array[cval] = array[child1]
                    array[child1] = temp
                    cval = child1
                else :
                    temp = array[cval]
                    array[cval] = array[child2]
                    array[child2] = temp
                    cval = child2
                child1 = 2*cval+1
                child2 = 2*cval+2
            else :
                break
        if child1<len(array) :
            if array[child1] < array[cval] :
                temp = array[cval]
                array[cval] = array[child1]
                array[child1] = temp

 
    def siftUp(self, index):
        cval = index
        while cval > 0:
            pval = (cval - 1) // 2  # Calculate the parent index using integer division
            if self.heap[pval] > self.heap[cval]:
                self.heap[pval], self.heap[cval] = self.heap[cval], self.heap[pval]
                cval = pval
            else:
                break

    def peek(self):
        if self.heap == [] :
            return -999999
        return self.heap[0]

    def remove(self):
        lastIndex = len(self.heap)-1
        temp = self.heap[0]
        self.heap[0] = self.heap[lastIndex]
        self.heap[lastIndex] = temp
        self.heap = self.heap[0:lastIndex]
        self.siftDown(0,self.heap)
        return temp

    def insert(self, value):
        self.heap.append(value)
        self.siftUp(len(self.heap)-1)