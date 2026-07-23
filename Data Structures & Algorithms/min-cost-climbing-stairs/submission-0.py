class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        from functools import cache
        @cache
        def solve(i):
            if i+2 >=len(cost):
                return 0
            return min(cost[i+1]+solve(i+1),cost[i+2]+solve(i+2))
        return min(cost[0]+solve(0),cost[1]+solve(1))