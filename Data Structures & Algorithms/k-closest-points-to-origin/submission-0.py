class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        heap=[]
        for x,y in points:
            d=-(x*x+y*y)

            if len(heap)==k:
                if d>heap[0][0]:
                    heapq.heappushpop(heap,(d,x,y))
            else:
                heapq.heappush(heap,(d,x,y))
        return [x[1:] for x in heap]
