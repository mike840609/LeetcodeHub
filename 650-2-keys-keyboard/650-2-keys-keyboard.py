class Solution:
    def minSteps(self, n: int) -> int:        
        if n == 1: return 0
        dp = [0] * (n+1) 
        dp[0] = 1
        prev = 1 
        
        for i in range(1, n+1):
            for j in range(i-1, 0, -1):
                if i%j == 0:
                    dp[i] = dp[j] + i//j
                    break
                    
        return dp[-1]
            