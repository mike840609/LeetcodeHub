class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:-1}
        s = 0 
        for i, n in enumerate(nums):
            if k != 0:
                s = (s+n) %k 
            else:
                s += n
            
            
            if s in d:
                if i - d[s] >= 2:
                    return True
                
            if s not in d:
                d[s] = i
            
        return False
    