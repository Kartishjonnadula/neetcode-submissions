class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        def find_order(a,b):
            for i,j in zip(a,b):
                if i!=j:
                    return i,j
            return -1,-1
        from collections import defaultdict
        indeg=defaultdict(int)
        adj=defaultdict(list)
        unq=set()
        for word in words:
            for c in word:
                indeg[c] = 0
                unq.add(c)
        for i in range(1,len(words)):
            k,j=find_order(words[i-1],words[i])
            if j!=-1:
                indeg[j]+=1
                adj[k].append(j)
            elif len(words[i])<len(words[i-1]):
                return ""
        q=deque()
        ans=[]
        for node in unq:
            if indeg[node]==0:
                ans.append(node)
                q.append(node) 
        while q:
            node=q.popleft()
            for nei in adj[node]:
                indeg[nei]-=1
                if indeg[nei]==0:
                    ans.append(nei)
                    q.append(nei)
        print(ans,unq)
        if len(ans)!=len(unq):
            return ""
        return "".join(ans)

