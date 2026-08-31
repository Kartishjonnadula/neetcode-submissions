class Solution:
    def maxProduct(self,nums):
        def solve():
            curr_max,curr_min=nums[0],nums[0]
            ans=nums[0]
            for i in nums[1:]:
                if i==0:
                    curr_min,curr_max=1,1
                elif i<0:
                    curr_min,curr_max=curr_max,curr_min
                curr_max=max(i,curr_max*i)
                curr_min=min(i,curr_min*i)
                ans=max(ans,curr_max)
                # print(curr_max,curr_min,ans)
            return ans
        return solve()