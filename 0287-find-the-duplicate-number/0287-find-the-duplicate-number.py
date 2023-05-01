class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        l = len(nums)
        
        i, j = 1, len(nums)-1
        
        while i < j: 
            m = (i+j) // 2 
            cnt = 0 
            for idx in range(l):
                if nums[idx] <= m:
                    cnt += 1 
            
            if cnt <= m:
                i = m + 1 
            else:
                j = m
            
        
        return i 
                                     
            
            