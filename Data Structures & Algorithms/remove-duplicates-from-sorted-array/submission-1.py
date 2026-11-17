class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums)<=1:
            return len(nums)
        curr=nums[0]
        i=1
        prev=1
        while i<len(nums):
            if nums[i]!=curr:
                curr=nums[i]
                nums[prev],nums[i]=curr,nums[prev]
                prev+=1
                i+=1
            else:
                i+=1
        return prev

            
        