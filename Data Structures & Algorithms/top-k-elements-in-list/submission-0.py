class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d=defaultdict(int)
        for i in nums:
            d[i]+=1
        a=[]
        for i in d:
            a.append((-d[i],i))
        heapq.heapify(a)
        print(a)
        res=[]
        for i in range(k):
            res.append(heapq.heappop(a)[1])
        return res

        