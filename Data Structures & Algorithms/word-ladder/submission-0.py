class Solution:
    def ladderLength(self, source: str, target: str, words: List[str]) -> int:
        # def are_they_connected(word1,word2):
        #     c=0
        #     for i,j in zip(word1,word2):
        #         if i!=j:
        #             c+=1
        #         if c==2:
        #             return False
        #     return True
        # adj=defaultdict(list)
        # nodes=[(i,wordList[i]) for i in range(len(wordList))]
        # for i in range(len(wordList)):
        #     for j in range(i+1,len(wordList)):
        #         if are_they_connected(wordList[i],wordList[j]):
        #             adj[i].append(j)
        #             adj[j].append(i)
        # print(adj)

        d={}
        for i in words:
            d[i]=1
        if target not in words:
            return 0
        q=deque()
        q.append(source)
        visited={}
        visited[source]=1
        ans=1
        while q:
            for _ in range(len(q)):
                source=q.popleft()
                for i in range(len(source)):
                    for c in range(ord('a'),ord('a')+26):
                        new_word=source[:i]+chr(c)+source[i+1:]
                        # print(new_word)
                        if new_word in d:
                            if new_word not in visited:
                                q.append(new_word)
                                visited[new_word]=1
                            if new_word==target:
                                return ans+1
            ans+=1
        return 0




