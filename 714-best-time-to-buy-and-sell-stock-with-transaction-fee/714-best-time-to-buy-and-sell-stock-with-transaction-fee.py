class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1 : return 0 
        
        buy = [0] * len(prices)
        sell = [0] * len(prices)        
        buy[0] = -prices[0]
        
        for i in range(1, len(prices)):
            # keep the same as day i-1, or buy from sell status at day i-1
            buy[i] = max(buy[i-1], sell[i-1] - prices[i])
            
            # keep the same as day i-1, or sell from buy status at day i-1
            sell[i] = max(sell[i-1], buy[i-1] + prices[i] - fee)
            
        return sell[-1]
            