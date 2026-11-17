class Solution:
    def merge(self, a: List[int], m: int, b: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        m-=1
        n-=1
        last=len(a)-1
        while n>=0 and m>=0:
            if a[m]>b[n]:
                a[last]=a[m]
                m-=1
                last-=1
            else:
                a[last]=b[n]
                n-=1
                last-=1
        while n>=0:
            a[last]=b[n]
            n-=1
            last-=1
        while m>=0:
            a[last]=a[m]
            m-=1
            last-=1
        
        