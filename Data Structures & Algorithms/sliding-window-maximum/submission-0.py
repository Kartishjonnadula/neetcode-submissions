class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q=deque()
        ans=[]
        for i in range(k):
            while q and q[0][0]<nums[i]:
                q.popleft()
            q.append((nums[i],i))
        if q:
            ans.append(q[0][0])
        for i in range(k,len(nums)):
            while q and q[0][0]<nums[i]:
                q.popleft()
            if q:
                _,idx=q[0]
            while q and idx<(i-k):
                q.popleft()
                _,idx=q[0]
            q.append((nums[i],i))
            if q:
                ans.append(q[0][0])
        return ans
                  