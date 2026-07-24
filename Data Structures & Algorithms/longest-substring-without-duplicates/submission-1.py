class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=-1
        res=0
        d={}
        n=len(s)
        last_seen=-1
        for end in range(n):
            if s[end] in d:
                last_seen=d[s[end]]
            start=max(last_seen,start)
            res=max(res,end-start)
            d[s[end]]=end
        return res
        