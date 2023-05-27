class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        cnt = 0
        m = {0: -1}
        res = 0        
        
        for idx, n in enumerate(nums):
            if n == 0:
                cnt += 1
            elif n == 1:
                cnt -= 1
            
            if cnt not in m:
                m[cnt] = idx
            
            if cnt in m:
                res = max(res, idx - m[cnt])
                
        return res
            