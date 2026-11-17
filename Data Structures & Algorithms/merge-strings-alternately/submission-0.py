class Solution:
    def mergeAlternately(self, a: str,b: str) -> str:
        n,m=len(a),len(b)
        i,j=0,0
        res=""
        while i<n and j<m:
            res+=a[i]+b[j]
            i+=1
            j+=1
        res+=a[i:]
        res+=b[j:]
        return res