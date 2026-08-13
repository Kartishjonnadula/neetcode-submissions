class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        from functools import cache
        @cache
        def solve(l,r):
            if l==r:
                return 0
            ans=0
            for k in range(l+1,r):
                ans=max(ans,solve(l,k)+solve(k,r)+(nums[l]*nums[k]*nums[r]))
            return ans
        nums=[1]+nums+[1]
        print(nums)
        return solve(0,len(nums)-1)