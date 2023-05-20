class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        dp = [0] * 10001
        
        for n in nums:
            dp[abs(n)] += 1
        
        res = [] 
        for i in range(10001):            
            res += [i**2] * dp[i]
        
        return res
            