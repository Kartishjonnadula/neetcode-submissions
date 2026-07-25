class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        directions=[(-1,0),(0,-1),(1,0),(0,1)]
        visited={}
        m=len(matrix)
        n=len(matrix[0])
        def dfs(i,j):
            if (i,j) in visited:
                return visited[(i,j)]
            ans=0
            for r,c in directions:
                if 0<=i+r<m and 0<=j+c<n:
                    if matrix[i][j]<matrix[i+r][j+c]:
                        ans=max(ans,1+dfs(i+r,j+c))
            visited[(i,j)]=ans
            return ans
        res=0
        for i in range(m):
            for j in range(n):
                res=max(res,dfs(i,j))
        return res+1
            