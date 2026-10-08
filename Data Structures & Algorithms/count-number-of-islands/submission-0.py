class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def mark(i,j):
            n=len(grid)
            m=len(grid[0])
            if grid[i][j]=="1":
                grid[i][j]=-1
            if i+1<n and grid[i+1][j]=="1":
                mark(i+1,j)
            if j+1<m and grid[i][j+1]=="1":
                mark(i,j+1)
            if i>0 and grid[i-1][j]=="1":
                mark(i-1,j)
            if j>0 and grid[i][j-1]=="1":
                mark(i,j-1)
        ans=0
        # print("hi",grid)
        for k in range(0,len(grid)):
            for l in range(0,len(grid[0])):
                if grid[k][l]=="1":
                    mark(k,l)
                    ans+=1
        return ans   