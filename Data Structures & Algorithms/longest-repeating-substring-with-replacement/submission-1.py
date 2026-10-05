class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        start=0
        max_freq=0
        from collections import defaultdict
        d=defaultdict(int)
        res=0
        for end in range(len(s)):
            d[s[end]]+=1
            max_freq=max(max_freq,d[s[end]])
            if (end-start+1)-max_freq>k:
                d[s[start]]-=1
                start+=1
        
            res=max(res,end-start+1)
        return res