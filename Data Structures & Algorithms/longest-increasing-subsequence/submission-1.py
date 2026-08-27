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
        # return solve(0,-1)

        dp=[[0]*(n+1) for _ in range(len(nums)+1)]
        for i in range(n-1,-1,-1):
            for j in range(i-1,-2,-1):
                k=j+1
                ans=-1
                if nums[i]>nums[j] or j==-1:
                    ans=1+dp[i+1][i+1]
                dp[i][k]=max(ans,dp[i+1][k])
        return dp[0][0]    






