class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        from math import inf
        from functools import cache
        @cache
        def solve(target):
            if target==0:
                return 0
            ans=inf
            for coin in coins:
                if target>=coin:
                     ans=min(ans,1+solve(target-coin))
            return ans
        # x=solve(amount)
        # return -1 if x==inf else x
        dp=[inf]*(amount+1)
        dp[0]=0
        for i in range(1,amount+1):
            ans=inf
            for coin in coins:
                if i>=coin:
                    ans=min(ans,1+dp[i-coin])
            dp[i]=ans
        if dp[amount]==inf:
            return -1
        return dp[amount]



