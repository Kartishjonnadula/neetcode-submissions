class Solution:
    def minDistance(self, s: str, t: str) -> int:
        from math import inf
        from functools import cache
        @cache
        def solve(i,j):
            if i==len(s) and j==len(t):
                return 0
            if i==len(s):
                return len(t[j:])
            if j==len(t):
                return len(s[i:]) 
            ans1,ans2,ans3,ans4=inf,inf,inf,inf
            if s[i]==t[j]:
                ans1=solve(i+1,j+1)
            # insert any character:
            ans2=1+solve(i,j+1)
            #delete a character
            ans3=1+solve(i+1,j)
            #replace any character
            ans4=1+solve(i+1,j+1)
            return min(ans1,ans2,ans3,ans4)
        # return solve(0,0)
        dp=[[inf]*(len(t)+1) for i in range(len(s)+1)]
        dp[len(s)][len(t)]=0
        for j in range(len(t)+1):
            dp[len(s)][j]=len(t[j:])
        for i in range(len(s)+1):
            dp[i][len(t)]=len(s[i:])
        # print(dp)
        for i in range(len(s)-1,-1,-1):
            for j in range(len(t)-1,-1,-1):
                ans1,ans2,ans3,ans4=inf,inf,inf,inf
                if s[i]==t[j]:
                    ans1=dp[i+1][j+1]
                ans2=1+dp[i][j+1]
                ans3=1+dp[i+1][j]
                ans4=1+dp[i+1][j+1]
                dp[i][j]=min(ans1,ans2,ans3,ans4)
        return dp[0][0]