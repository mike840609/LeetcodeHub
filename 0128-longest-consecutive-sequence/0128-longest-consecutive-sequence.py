class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0 
        
        for n in nums:
            if n not in s: continue 
            
            min_, max_ = n, n
            
            s.remove(n)
            
            while min_-1 in s:
                min_ -= 1
                s.remove(min_)
            
            while max_+1 in s:
                max_ += 1
                s.remove(max_)
            
            
            res = max(res, max_-min_+1)
        
        return res
                
                