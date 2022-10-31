class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        b = len(nums)-1
        r,w = 0, 0
        
        
        while w <= b:
            if nums[w] == 0 :
                nums[r], nums[w] = nums[w], nums[r]
                r += 1
                w += 1
                
            elif nums[w] == 2:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1
                            
            elif nums[w] == 1:
                w += 1
                
        
            