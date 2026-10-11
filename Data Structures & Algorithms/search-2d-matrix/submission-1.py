class Solution:
    def searchMatrix(self, a: List[List[int]], target: int) -> bool:
        def find(n,m):
            r,c=n,0
            # print(r,c)
            while r>=0 and c<=m:
                if a[r][c]==target:
                    return True
                elif a[r][c]<target:
                    c+=1
                else:
                    r-=1
                # print(r,c)
            return False
        return find(len(a)-1,len(a[0])-1)
        