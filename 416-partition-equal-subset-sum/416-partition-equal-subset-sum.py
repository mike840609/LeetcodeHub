class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        
        if s&1: return False 
                
        target = s//2                        
    
        seen = {0}
        
        for n in nums:
            tmp = set()
            for k in seen:
                if k+n < target:
                    tmp.add(k+n)
                elif k+n == target:
                    return True
                
            seen |= tmp
            
        return False 
                
            