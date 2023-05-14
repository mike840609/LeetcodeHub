class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        if not nums: return []
        
        nums.sort()        
        res, cur = [[]], []
        
        for i, n in enumerate(nums):
            if i > 0 and nums[i-1] == n:
                cur = [x + [n] for x in cur]
            
            else:
                cur = [x + [n] for x in res]
            
            res += cur 
            
            
        return res
                
        