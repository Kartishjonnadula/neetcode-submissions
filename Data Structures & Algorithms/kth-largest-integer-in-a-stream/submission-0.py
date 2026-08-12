class KthLargest:
    import heapq
    def __init__(self, k: int, nums: List[int]):
        self.k=k
        a=[]
        for val in nums:
            if len(a)==self.k:
                if a[0]<val:
                    heapq.heappop(a)
                    heapq.heappush(a,val)
            else:
                heapq.heappush(a,val)
        self.nums=a
        

    def add(self, val: int) -> int:
        if len(self.nums)==self.k:
            if self.nums[0]<val:
                heapq.heappop(self.nums)
                heapq.heappush(self.nums,val)
            
        else:
            heapq.heappush(self.nums,val)
        return self.nums[0]