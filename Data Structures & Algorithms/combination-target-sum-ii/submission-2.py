class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        ans=[]
        def solve(start,target,curr):
            # print(curr,target)
            if target==0:
                ans.append(curr[:])
                return
            if start>=len(nums) or target<0:
                return
            x=len(curr)
            for i in range(start,len(nums)):
                if i>start and nums[i]==nums[i-1]:
                    continue
                curr.append(nums[i])
                solve(i+1,target-nums[i],curr)
                curr.pop()
            return 
                

        nums.sort()
        solve(0,target,[])
        return ans
