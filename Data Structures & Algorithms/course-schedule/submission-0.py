class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        from collections import deque,defaultdict
        graph=defaultdict(list)
        degree=defaultdict(int)
        n=numCourses
        a=prerequisites
        for i,j in a:
            graph[j].append(i)
            degree[i]+=1
        queue=deque()
        visited=[]
        for i in range(n):
            if degree[i]==0:
                queue.append(i)
        completed=0
        while queue:
            node=queue.popleft()
            completed+=1
            for nextnode in graph[node]:
                degree[nextnode]-=1
                if degree[nextnode]==0 :
                    queue.append(nextnode)

        return completed==n

        