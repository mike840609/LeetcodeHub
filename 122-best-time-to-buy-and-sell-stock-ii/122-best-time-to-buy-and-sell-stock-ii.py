class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        not_hold, hold = 0, float('-inf')
        
        for p in prices:
            not_hold, hold = max(not_hold, hold+p), max(hold, not_hold-p)
        
        return not_hold