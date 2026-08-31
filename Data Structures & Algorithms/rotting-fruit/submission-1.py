class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
                
        from collections import deque
        fresh=0
        q=deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
                elif grid[i][j]==1:
                    fresh+=1
        dir=[(0,1),(0,-1),(1,0),(-1,0)]
        time=0
        if fresh==0:
            return time
        while q:
            time+=1
            for _ in range(len(q)):
                i,j=q.popleft()
                for r,c in dir:
                    if 0<=i+r<len(grid) and 0<=j+c<len(grid[0]):
                        if grid[i+r][j+c]==1:
                            grid[i+r][j+c]=2
                            fresh-=1
                            q.append((i+r,j+c))
                            if fresh==0:
                                return time
        return -1
