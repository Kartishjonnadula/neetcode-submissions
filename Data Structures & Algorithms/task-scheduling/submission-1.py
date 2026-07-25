class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import defaultdict
        import heapq
        d=defaultdict(int)
        for task in tasks:
            d[task]+=1
        heap=[(-d[i],i) for i in d]
        heapq.heapify(heap)
        ans=0
        while heap:
            tempcount=0
            rem=[]
            for i in range(n+1):
                if heap:
                    count,task=heapq.heappop(heap)
                    count+=1
                    if count<0:
                        rem.append((count,task))
                    tempcount+=1
                    # print(task)
                else:
                    break
            if rem:
                # print(rem)
                for i in rem:
                    heapq.heappush(heap,i)
                ans+=n+1
            else:
                ans+=tempcount
        return ans
                