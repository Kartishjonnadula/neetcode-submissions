class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        from functools import cache
        @cache
        def solve(i,n):
            if i>=n:
                return 0
            ans1,ans2=0,0
            ans1=nums[i]+solve(i+2,n)
            ans2=solve(i+1,n)
            return max(ans1,ans2)
        return max(solve(0,n-1),solve(1,n))