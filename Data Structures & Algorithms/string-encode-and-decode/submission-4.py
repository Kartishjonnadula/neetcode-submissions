class Solution:

    def encode(self, strs: List[str]) -> str:
        res=""
        for i in strs:
            res+=str(len(i))+'#'+i
        print(res)
        return res

        

    def decode(self, s: str) -> List[str]:
        i=0
        print(s)
        res=[]
        while i<len(s):
            count=0
            while s[i]!="#":
                count=count*10+int(s[i])
                i+=1
            i+=1
            res.append(s[i:i+count])
            i+=count
        return res
