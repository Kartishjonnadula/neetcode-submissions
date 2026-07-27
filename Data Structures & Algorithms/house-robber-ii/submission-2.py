class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        self.nums=nums
        if n==1:
            return sum(nums)
        from functools import cache
        def solve(i,n):
            if i>=n:
                return 0
            ans1,ans2=0,0
            if i==n-1 and nums[0]==-1:
                return 0
            t=self.nums[i]
            self.nums[i]=-1
            ans1=t+solve(i+2,n)
            self.nums[i]=t
            ans2=solve(i+1,n)
            return max(ans1,ans2)
        # return max(solve(0,n-1),solve(1,n))
        return solve(0,n)