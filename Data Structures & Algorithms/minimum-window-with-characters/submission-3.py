class Solution:
    def minWindow(self, s: str, t: str) -> str:
        from collections import defaultdict
        if len(t)>len(s):

            return "" 
        missing=len(t)
        d=defaultdict(int)
        for i in t:
            d[i]+=1
        start,ans=0,s
        f=0
        for end in range(0, len(s)):
            d[s[end]]-=1
            if d[s[end]]>=0:
                missing-=1
            # print(missing)
            while missing==0:
                curr=s[start:end+1]
                ans=curr if len(curr)<len(ans) else ans
                d[s[start]]+=1
                if d[s[start]]>0:
                    missing+=1
                start+=1
                f=1
            
        return ans if f==1 else ""
                
            
        