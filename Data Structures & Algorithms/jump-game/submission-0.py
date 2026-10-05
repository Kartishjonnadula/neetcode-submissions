class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest=nums[0]
        for i,jump in enumerate(nums):
            if i>farthest:
                return False
            farthest=max(farthest,jump+i)
        return True             

        