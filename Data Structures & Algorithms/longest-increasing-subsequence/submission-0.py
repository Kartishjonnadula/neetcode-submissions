class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n=len(nums)
        
        dp=defaultdict(lambda : -1)
        def solve(i,prev):
            if dp[(i,prev)]!=-1:
                return dp[(i,prev)]
            if i==n:
                return 0
            ans=0
            if nums[i]>nums[prev] or prev==-1:
                ans=1+solve(i+1,i)
            dp[(i,prev)]=max(ans,solve(i+1,prev))
            return dp[(i,prev)]
        return solve(0,-1)