class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_ = float('inf')
        mid_ = float('inf')
        
        for n in nums:
            if n < min_:
                min_ = n 
            
            elif min_ < n < mid_:
                mid_ = n                
            
            elif n > mid_:
                return True
        
        return False
        