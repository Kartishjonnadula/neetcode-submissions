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
        return solve(0,0)
             
        