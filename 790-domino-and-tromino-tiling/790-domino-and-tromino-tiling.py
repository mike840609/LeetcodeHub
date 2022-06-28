class Solution:
    def numTilings(self, n: int) -> int:
        
        dp = [0] * max((n+1), 4)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2        
        mod = 10**9 + 7
        
        for i in range(3, n+1):
            dp[i] += dp[i-1]
            dp[i] += dp[i-2]
            dp[i] += 2 * sum(dp[0:i-2])
            dp[i] %= mod
            
        return dp[n] % mod
            
        