class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if len(nums) == 0 : return 0 
        s = sum(nums)
        s1 = ((1 + len(nums)) * len(nums)) // 2        
        return s1 - s
                
        