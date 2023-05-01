class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0 
        for i, n in enumerate(nums):            
            xor = xor ^ (i+1) ^ n 
        return xor 
                
        