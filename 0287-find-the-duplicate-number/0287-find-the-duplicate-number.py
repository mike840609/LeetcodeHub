class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for i, n in enumerate(nums):            
            idx = abs(n)            
            if nums[idx] < 0:
                return idx
            
            nums[idx] *= -1
                    
        return -1
                                     
            
            