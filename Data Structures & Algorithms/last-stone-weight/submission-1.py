class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq
        stones=[-1* stone for stone in stones]
        heapq.heapify(stones)
        while len(stones)>1:
            x=-heapq.heappop(stones)
            y=-heapq.heappop(stones)
            x,y=max(x,y),min(x,y)
            new_stone=x-y
            if new_stone!=0:
                heapq.heappush(stones,-new_stone)
            
        return  -stones[0] if stones else 0