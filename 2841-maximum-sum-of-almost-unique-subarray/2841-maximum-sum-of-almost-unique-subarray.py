# Pair wise distinct count = unique char count

class Solution:
    def maxSum(self, nums: List[int], m: int, k: int) -> int:
        res, s = 0, 0        
        c = Counter()        
                                                
        for i, x in enumerate(nums):            
            s += x 
            c[x] += 1                                    
                                    
            if i > k - 1:
                p = nums[i-k]
                s -= p 
                c[p] -= 1
                    
                if c[p] == 0:
                    del c[p]
                                        
            if len(c.keys()) >= m:                
                res = max(res, s)
                
        return res                                                                    