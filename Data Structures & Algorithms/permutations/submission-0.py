class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def solve(i):
            if i==len(nums):
                ans.append(nums[:])
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]
                solve(i+1)
                nums[i],nums[j]=nums[j],nums[i]
            return
        solve(0)
        return ans
                
        