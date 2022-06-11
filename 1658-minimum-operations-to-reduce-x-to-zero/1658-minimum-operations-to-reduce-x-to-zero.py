class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        acc = [0] + list(accumulate(nums))        
        dp = {val:i for i, val in enumerate(acc)}        
        goal = acc[-1] - x 
        
        
        if goal < 0 :
            return -1 
        
        res = -sys.maxsize
        
        for num, idx in dp.items():
            if num + goal in dp:
                idx2 = dp[num+goal]
                res = max(res, idx2 - idx)
        
        return len(nums) - res if res != -sys.maxsize else -1
            
        