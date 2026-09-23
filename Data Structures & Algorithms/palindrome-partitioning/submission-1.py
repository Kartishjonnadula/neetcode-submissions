class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ans=[]
        def is_pal(s):
            return s==s[::-1]
        def solve(arr,i):
            if i==len(s):
                self.ans.append(arr[:])
            curr=""
            for i in range(i,len(s)):
                curr+=s[i]
                if curr==curr[::-1]:
                    arr.append(curr)
                    solve(arr,i+1)
                    arr.pop()
        solve([],0)
        return self.ans

            