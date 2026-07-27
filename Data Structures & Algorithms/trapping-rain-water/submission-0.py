class Solution:
    def trap(self, height: List[int]) -> int:
        lmax=0
        rmax=0
        start,end=0,len(height)-1
        ans=0
        while start<end:
            if height[start]<height[end]:
                lmax=max(height[start],lmax)
                ans+=lmax-height[start]
                start+=1
            else:
                rmax=max(height[end],rmax)
                ans+=rmax-height[end]
                end-=1
        return ans