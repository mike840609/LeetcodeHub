class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        def dfs(n):
            if n == 0 :
                return False 
            
            if n in dp:
                return dp[n]            
            
            # we could choose any i which i*i < n
            for i in range(1, int(n**0.5) + 1):
                if not dfs(n - i*i):
                    dp[n] = True
                    return dp[n]
            dp[n] = False
            
            return dp[n]
        
        dp = {}
        dfs(n)
        return dp[n]