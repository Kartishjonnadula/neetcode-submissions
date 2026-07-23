class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        class DSU:
            def __init__(self,n):
                self.parent=[i for i in range(n+1)]
            def find(self,x):
                if self.parent[x]!=x:
                    self.parent[x]=self.find(self.parent[x]) 
                return self.parent[x]
            def union(self,x,y):
                p1=self.find(x)
                p2=self.find(y)
                self.parent[p1]=p2
        dsu=DSU(len(edges))
        for x,y in edges:
            if dsu.find(x)==dsu.find(y):
                return [x,y]
            dsu.union(x,y)

        