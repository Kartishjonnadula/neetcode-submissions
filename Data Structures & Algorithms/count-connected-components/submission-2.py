class Solution:

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        class DSU:
            def __init__(self,n):
                self.parent=[i for i in range(n)]
                self.size=[1 for i in range(n)]
            def find(self,x):
                if self.parent[x]!=x:
                    self.parent[x]=self.find(self.parent[x])
                return self.parent[x]
            def union(self,x,y):
                pa=self.find(x)
                pb=self.find(y)
                if self.size[pa]>self.size[pb]:
                    self.parent[pb]=pa
                    self.size[pa]+=self.size[pb]
                else:
                    self.parent[pa]=pb
                    self.size[pb]+=self.size[pa]
                return
        dsu=DSU(n)
        for i,j in edges:
            dsu.union(i,j)
        s=set()
        for i in range(n):
            s.add(dsu.find(i))
        return len(s) 
            