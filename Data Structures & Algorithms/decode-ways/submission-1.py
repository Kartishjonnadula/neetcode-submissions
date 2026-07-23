class Solution:
    def numDecodings(self, s: str) -> int:
        from functools import cache
        @cache
        def solve(i):
            if i==len(s):
                return 1
            
            ans=0
            if s[i]==0:
                return 0
            if 1<=s[i]<=9:
                ans+=solve(i+1)
            if i<len(s)-1 and 10<=(s[i]*10+s[i+1])<=26:
                ans+=solve(i+2)
            
            return ans
        s=[int(i) for i in s]
        return solve(0)