class Solution:
    def jump(self, nums: List[int]) -> int:
        far=0
        curr_end=0
        ans=0
        n=len(nums)
        for i in range(n-1):
            far=max(i+nums[i],far)
            if i==curr_end:
                ans+=1
                curr_end=far
        return ans
        