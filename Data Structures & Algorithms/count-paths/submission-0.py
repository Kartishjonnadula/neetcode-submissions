class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        from functools import cache
        @cache
        def solve(i,j):
            if i==n-1 and j==m-1:
                return 1
            directions=[(1,0),(0,1)]
            ans=0
            for r,c in directions:
                if 0<=i+r<n and 0<=j+c<m:
                    ans+=solve(i+r,j+c)
            return ans
        # return solve(0,0)
        directions=[(1,0),(0,1)]
        dp=[[0]*n for i in range(m)]
        dp[m-1][n-1]=1
        for i in range(n):
            dp[m-1][i]=1
        for j in range(m):
            dp[j][n-1]=1
        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                ans=0
                for r,c in directions:
                    if 0<=i+r<m and 0<=j+c<n:
                        ans+=dp[i+r][j+c]
                dp[i][j]=ans
        return dp[0][0]

