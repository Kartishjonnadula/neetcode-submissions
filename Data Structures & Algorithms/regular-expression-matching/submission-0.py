class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        d=[0]*len(p)
        for i,val in enumerate(p):
            if val=='*':
                d[i-1]=1
        # p=[i for i in p if i!='*']
        print(d)
        n=len(s)
        m=len(p)
        from functools import cache
        @cache
        def solve(i,j):
            if i==n and j==m:
                return True
            if j>=m:
                return False
            ans1,ans2=False,False
            match=i<n and (s[i]==p[j] or p[j]==".")
            if match:
                ans1=solve(i+1,j+1)
            if j+1<m and p[j+1]=='*':
                ans2=solve(i,j+2) or (match and solve(i+1,j))
            return ans1 or ans2 
        # return solve(0,0)
        dp=[[False]* (m+2) for i in range(n+2)]
        dp[n][m]=True
        for j in range(m-2,-1,-1):
            if p[j+1]=='*':
                dp[n][j]=dp[n][j+2]
        for i in range(n-1,-1,-1):
            for j in range(m-1,-1,-1):
                ans1,ans2=False,False
                match=i<n and (s[i]==p[j] or p[j]=='.')
                if match:
                    ans1=dp[i+1][j+1]
                if j+1<m and p[j+1]=='*':
                    ans2=dp[i][j+2] or (match and dp[i+1][j])
                dp[i][j]=ans1 or ans2
        return dp[0][0]
            
            