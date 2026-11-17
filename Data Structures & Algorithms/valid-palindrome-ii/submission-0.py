class Solution:
    def validPalindrome(self, s: str) -> bool:
        def solve(l,r,f):
            while l<r:
                if s[l]!=s[r]:
                    if f==1:
                        return False
                    return solve(l+1,r,1) or solve(l,r-1,1)
                l+=1
                r-=1
            return True            
        return solve(0,len(s)-1,0)