class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        snowBall = 0 
        for i in range(len(nums)):
            if nums[i] == 0:
                snowBall += 1
            elif snowBall > 0 and nums[i] != 0:
                t = nums[i]
                nums[i] = 0 
                nums[i-snowBall] = t
                
                
        
            
            
                
            
                
            
        
        