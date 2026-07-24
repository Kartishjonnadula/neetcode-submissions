class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        from math import inf
        distance=[inf]*n
        distance[src]=0
        for _ in range(k+1):
            temp=distance[:]
            for a,b,cost in flights:
                temp[b]=min(temp[b],distance[a]+cost)
            distance=temp
        return distance[dst] if distance[dst]!=inf else -1
                