class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        start=0
        if len(s1)>len(s2):
            return False
        missing=len(s1)
        d=defaultdict(int)
        for i in s1:
            d[i]+=1
        for end in range(0,len(s2)):
            d[s2[end]]-=1
            if d[s2[end]]>=0:
                missing-=1
            else:
                while d[s2[end]]<0:
                    d[s2[start]]+=1
                    if d[s2[start]]>0:
                        missing+=1
                    start+=1
            if missing==0:
                return True
        return False

        