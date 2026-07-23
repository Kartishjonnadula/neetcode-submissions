class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        from collections import defaultdict
        start=0
        max_freq=0
        res=0
        d=defaultdict(int)
        for end in range(start,len(s)):
            d[s[end]]+=1
            max_freq=max(max_freq,d[s[end]])
            while (end-start+1)-max_freq>k:
                d[s[start]]-=1
                start+=1
            res=max(res,end-start+1)
        return res
            