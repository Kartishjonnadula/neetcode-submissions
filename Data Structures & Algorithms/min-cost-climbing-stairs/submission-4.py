class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        from functools import cache
        from math import inf
        # @cache
        # def solve(i):
        #     if i+2 >=len(cost):
        #         return 0
        #     return min(cost[i+1]+solve(i+1),cost[i+2]+solve(i+2))
        # # return min(cost[0]+solve(0),cost[1]+solve(1))   
        dp=[inf]*(len(cost)+3)
        # dp[0]=cost[0]
        # dp[1]=cost[1]
        # for i in range(2,len(cost)):
        #     dp[i]=cost[i]+min(dp[i-1],dp[i-2])
        # return min(dp[len(cost)-1],dp[len(cost)-2])
        dp[len(cost)-1]=0
        dp[len(cost)-2]=0
        # dp[len(cost)-2]=cost[-2]
        for i in range(len(cost)-3,-1,-1):
            dp[i]=min(cost[i+1]+dp[i+1],cost[i+2]+dp[i+2])
        return min(cost[0]+dp[0],cost[1]+dp[1])