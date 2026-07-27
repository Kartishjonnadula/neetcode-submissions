class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        # from functools import cache
        # @cache
        # def solve(i):
        #     if i>=n:
        #         return 0
        #     ans1,ans2=0,0
        #     ans1=nums[i]+solve(i+2)
        #     ans2=solve(i+1)
        #     return max(ans1,ans2)
        # return solve(0)
        
        # dp=[0]*(n+2)
        # for i in range(n-1,-1,-1):
        #     ans1,ans2=0,0
        #     ans1=nums[i]+dp[i+2]
        #     ans2=dp[i+1]
        #     dp[i]=max(ans1,ans2)
        # return dp[0]
        next1,next2=0,0
        for i in range(n-1,-1,-1):
            ans1=nums[i]+next2
            ans2=next1
            next2=next1
            next1=max(ans1,ans2)
        return next1
        