class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        from functools import cache
        @cache
        def solve(i,j):
            if i==len(text1) or j==len(text2):
                return 0
            ans1=0
            if text1[i]==text2[j]:
                ans1=1+solve(i+1,j+1)
            return max(ans1,solve(i+1,j),solve(i,j+1))
        # return solve(0,0)
         
        n=len(text1)
        m=len(text2)
        dp=[[0]*(m+1) for _ in range(n+1)] 
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                ans1=0
                if text1[i]==text2[j]:
                    ans1=1+dp[i+1][j+1]
                dp[i][j]=max(ans1,dp[i+1][j],dp[i][j+1])
        return dp[0][0]


        



             
        