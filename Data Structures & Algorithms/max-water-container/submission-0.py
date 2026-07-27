class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        a=height
        i,j=0,n-1
        area=min(a[0],a[n-1])*(n-1)
        while(i<j):
            area=max(area,(j-i)*(min(a[i],a[j])))
            if a[i]>a[j]:
                j-=1
            else:
                i+=1
        return area           
