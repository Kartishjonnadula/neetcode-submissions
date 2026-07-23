class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n=len(nums)
        from functools import cache
        @cache
        def solve(i,target):
            print(i,target)
            if i==n and target==0:
                print("aaf")
                return 1
            if i==n and target!=0:
                return 0
            ans=0
            ans+=solve(i+1,target-nums[i])
            ans+=solve(i+1,target+nums[i])    
            return ans
        return solve(0,target)