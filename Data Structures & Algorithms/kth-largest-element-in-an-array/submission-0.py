class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        nums=[-num for num in nums]
        heapq.heapify(nums)
        for _ in range(k):
            val=heapq.heappop(nums)
        return -val