class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        
        def solve(n,edges):
            from collections import defaultdict,deque
            adj=defaultdict(list)
            for i,j in edges:
                adj[i].append(j)
                adj[j].append(i)
            q=deque()
            q.append((0,-1))
            visited={0}
            c=0
            while q:
                for _ in range(len(q)):
                    node,parent=q.popleft()
                    c+=1
                    for nei in adj[node]:
                        if nei==parent:
                            continue
                        if nei in visited:
                            return False
                        q.append((nei,node))
                        visited.add(nei)

                            
                        
            return len(visited)==n
        return solve(n,edges)


