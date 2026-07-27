class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        def solve(i):
            if i>=n:
                return 0
            ans1,ans2=0,0
            ans1=nums[i]+solve(i+2)
            ans2=solve(i+1)
            return max(ans1,ans2)
        return solve(0)
        

        