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
        return solve(0,0)