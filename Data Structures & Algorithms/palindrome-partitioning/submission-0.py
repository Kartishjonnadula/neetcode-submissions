class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        ans=[]
        split=[]
        from functools import cache
        def solve(i):
            if i>=n:
                ans.append(split[:])
                return  
            curr=""
            for i in range(i,n):
                curr+=s[i]
                if curr==curr[::-1]:
                    split.append(curr)
                    solve(i+1)
                    split.pop()
            return
        solve(0)
        return ans

