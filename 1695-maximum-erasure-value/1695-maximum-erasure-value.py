class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        prefix = [0] + list(accumulate(nums))
        i = 0 
        d = {}
        res = 0
        # print(prefix)
        # print(nums)
        
        for idx, val in enumerate(nums):            
            if val in d and d[val] >= i:
                i = d[val]
                
            d[val] = idx + 1        
            res = max(res, prefix[idx+1] - prefix[i])
                        
            
        return res 
            
                
                
        