class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def solve(i,curr,curr_sum):
            if curr_sum==0:
                ans.append(curr[:])
                return
            if i>=len(nums) or curr_sum<0:
                return
            for i in range(i,len(nums)):
                curr.append(nums[i])
                solve(i,curr,curr_sum-nums[i])
                curr.pop()
            return 
        solve(0,[],target)
        return ans