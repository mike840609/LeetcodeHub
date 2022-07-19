class Solution:
    def reverse(self, x: int) -> int:
        sign = 1 if x >= 0 else -1 
        x = abs(x)
        
        res = 0 
        while x : 
            res *= 10 
            res += x%10 
            x //= 10
        
        return res * sign if  -2** 31 <= res * sign  <= 2**31 -1 else 0 
        
        
        