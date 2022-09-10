class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:        
        # [buy, sell]
        
        if k == 0: return 0        
        dp = [[-float('inf'), 0] for _ in range(k) ] 
        
        for p in prices :
            for i in range(k):
                if i == 0 :
                    dp[i][0] = max(dp[i][0], -p)
                    dp[i][1] = max(dp[i][1], dp[i][0] + p)
                
                else:
                    dp[i][0] = max(dp[i][0], dp[i-1][1] - p)
                    dp[i][1] = max(dp[i][1], dp[i][0] + p)
        return dp[-1][1]
                
        