class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def solve(i,curr):
            nonlocal ans
            if i>=len(nums):
                if curr not in ans:
                    ans.append(curr[:])
            for i in range(i,len(nums)):
                solve(i+1,curr)
                curr.append(nums[i])
                solve(i+1,curr)
                curr.pop()
            return
        solve(0,[])     
        return ans
        