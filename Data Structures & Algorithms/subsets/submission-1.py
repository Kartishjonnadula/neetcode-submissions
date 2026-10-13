class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def solve(i,curr):
            nonlocal ans
            print(i)
            if i>=len(nums):
                ans.append(curr[:])
                return
            solve(i+1,curr)
            curr.append(nums[i])
            solve(i+1,curr)
            curr.pop()
            return
        solve(0,[])     
        return ans
        