class Solution:
    def partitionArray(self, nums, k):
        if k == 0 : return len(set(nums))
        nums = list(set(nums))
        nums = sorted(nums)
        
        sIdx = 0
        res = 1 
        for i in range(1,len(nums)):
            if nums[i] - nums[sIdx] > k:
                sIdx = i 
                res += 1
        return res
            
            