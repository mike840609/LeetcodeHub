class Solution:
    def numTilings(self, n: int) -> int:
        dp = [0] * max(n+1, 4)
        dp[0] = 1
        dp[1] = 1
        dp[2] = 2
        mod = 10**9 + 7
        
        tmp = 0 
        for i in range(3, n+1):
            dp[i] += dp[i-1] + dp[i-2]
            tmp += dp[i-3]
            dp[i] += tmp * 2 
            dp[i] %= mod
        
        return dp[n]