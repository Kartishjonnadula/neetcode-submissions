class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        a=[]
        res=[0 for i in t]
        for i,v in enumerate(t):
            if len(a)==0:
                a.append((v,i))
                continue
            ans=1
            while len(a)!=0:
                x,y=a[-1]
                if x<v:
                    a.pop()
                    res[y]=i-y
                else:
                    break
            a.append((v,i))
        return res
                    
                    
