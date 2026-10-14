class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def solve(start,curr):
            ans.append(curr[:])
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                curr.append(nums[i])
                solve(i+1,curr)
                curr.pop()
            return
        ans=[]
        nums.sort()
        solve(0,[]) 
        return ans