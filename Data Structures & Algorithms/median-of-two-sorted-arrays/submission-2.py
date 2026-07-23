class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1):
            return self.findMedianSortedArrays(nums2,nums1)
        start=0
        end=len(nums1)
        n,m=len(nums1),len(nums2)
        median=(n+m+1)//2
        # 1 2 3 4 5 6.  median=5
        # 3 4 5 6 7.   
        while start<=end:
            mid=(start+end)//2
            rem=median-mid
            l1=nums1[mid-1] if mid>0 else float('-inf')   
            l2=nums2[rem-1] if rem>0 else float('-inf')
            r1=nums1[mid] if mid<len(nums1) else float('inf')
            r2=nums2[rem] if rem<len(nums2) else float('inf')
            if l1<=r2 and l2<=r1:
                if (m+n)%2==0:
                    return (max(l1,l2)+min(r1,r2))/2
                else:
                    return max(l1,l2)
            else:
                if l1>r2 and l2<r1:
                    end=mid-1
                else:
                    start=mid+1


