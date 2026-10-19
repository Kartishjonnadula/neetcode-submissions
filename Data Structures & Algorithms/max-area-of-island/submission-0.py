class Solution:
    def maxAreaOfIsland(self, a: list[list[int]]) -> int:
        def solve(i,j):
            if a[i][j] !=1:
                return 0
            a[i][j]=-1
            directions=[[1,0],[-1,0],[0,1],[0,-1]]
            ans=1
            for l,m in directions:
                x=i+l
                y=j+m
                if 0<=x<len(a) and 0<=y<len(a[0]) and a[x][y]==1:
                    ans+=solve(x,y)
            return ans
        res=0
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j]==1:
                    x=solve(i,j)
                    # print(x,i,j)
                    res=max(res,x)
        return res