class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start=-1
        res=0
        d=defaultdict(int)
        n=len(s)
        for end in range(n):
            last_seen=d[s[end]]
            start=max(last_seen,start)
            res=max(res,end-start)
            d[s[end]]=end
        return res
        