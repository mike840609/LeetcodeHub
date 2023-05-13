class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = Counter()
        dp[0] = 0 
        
        
        for i in range(amount+1):            
            for c in coins:            
                if i-c in dp:
                    dp[i] = min(dp[i-c]+1, dp[i]) if dp[i] != 0 else dp[i-c]+1
                    
        return dp[amount] if amount in dp else -1
        
                