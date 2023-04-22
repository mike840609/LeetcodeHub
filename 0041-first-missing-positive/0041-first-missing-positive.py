class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            
            x = nums[i]            
            
            if 1 <= x < len(nums) and nums[x-1] != x:                
                
                nums[i], nums[x-1] = nums[x-1], x
                
            else:                
                i += 1
                        
            
        for i, x in enumerate(nums, 1):
            if i != x:
                return i
        return len(nums)+1