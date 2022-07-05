class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        res = 0 
        for n in nums:
            if n-1 not in nums:
                cur = n
                while cur + 1 in nums:                    
                    cur += 1
                res = max(cur - n + 1, res)
            
        return res
                                                                                
        