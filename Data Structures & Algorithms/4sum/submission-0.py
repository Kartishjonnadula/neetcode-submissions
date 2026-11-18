class Solution:
    def fourSum(self, nums: list[int], target: int) -> list[list[int]]:
        nums.sort()
        ans=[]
        for i in range(len(nums)-3):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)-2):
                if j>i+1 and nums[j]==nums[j-1]:
                    # print("here")
                    continue
                req=target-(nums[i]+nums[j])
                l,r=j+1,len(nums)-1
                while l<r:
                    x=nums[l]+nums[r]
                    if x==req:
                        ans.append([nums[i],nums[j],nums[l],nums[r]])
                        while l<r and nums[l+1]==nums[l]:
                            l+=1
                        while r>l and nums[r-1]==nums[r]:
                            r-=1
                        l+=1
                        r-=1
                    elif x>req:
                        r-=1
                    else:
                        l+=1
        return ans
        