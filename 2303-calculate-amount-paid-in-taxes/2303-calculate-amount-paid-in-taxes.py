class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        prev, res = 0, 0 
        
        for hi, pct in brackets:
            hi = min(hi, income)
            res += (hi - prev) * (pct/100)
            prev = hi
            
        return res 