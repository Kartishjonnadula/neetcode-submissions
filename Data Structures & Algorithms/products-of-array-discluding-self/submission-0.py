class Solution:
    def productExceptSelf(self, a: List[int]) -> List[int]:
        i,j=0,len(a)-1
        start,end=1,1
        ans=[1 for i in range(len(a))]
        while i<len(a) and j>=0:
            t1,t2=a[i],a[j]
            ans[i]=ans[i]*start
            ans[j]=ans[j]*end
            start=start*t1
            end=end*t2
            i+=1
            j-=1
        return ans