class Solution:
    def numTrees(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 1 
        
        for i in range(1, n+1):
            for j in range(i):
                dp[i] += dp[j] * dp[i-j-1]
        
        return dp[n]
    

'''
class Solution:
    def numTrees(self, n: int) -> int:
        @lru_cache(None)
        def dp(n):
            if n <= 1:
                return 1
            elif n == 2:
                return 2 
            
            res = 0 
            for i in range(n):                
                res += dp(i) * dp(n-i-1)
            return res 
        
        return dp(n)
'''