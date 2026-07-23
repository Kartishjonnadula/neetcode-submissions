class MedianFinder:

    def __init__(self):
        self.maxheap=[]
        self.minheap=[]
        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap,-num)
        if len(self.maxheap)>len(self.minheap):
            heapq.heappush(self.minheap,-heapq.heappop(self.maxheap))
        if len(self.minheap)>len(self.maxheap):    
            heapq.heappush(self.maxheap,-heapq.heappop(self.minheap))
        # print(self.maxheap,self.minheap)
        


    def findMedian(self) -> float:
        if (len(self.maxheap)+len(self.minheap))%2==0:
            return (-self.maxheap[0]+self.minheap[0])/2
        else:
            return -self.maxheap[0]
        