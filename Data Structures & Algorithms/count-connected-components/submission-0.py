class Solution:
    class uf:
        def __init__(self,n):
            self.parent=[i for i in range(n)]
            self.components=n
            self.size=[1]*n
        def find(self,x):
            if self.parent[x]!=x:
                self.parent[x]=self.find(self.parent[x])
            return self.parent[x]
        def union(self,a,b):
            pa=self.find(a)
            pb=self.find(b)
            if pa==pb:
                # alr connected
                return 
            if self.size[pa]<self.size[pb]:
                return self.union(b,a)
            self.parent[pb]=pa
            self.size[pa]+=self.size[pb]
            self.size[pb]=self.size[pa]
            self.components-=1
            return

    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        union_find=self.uf(n)
        for i,j in edges:
            union_find.union(i,j)
        return union_find.components            
        