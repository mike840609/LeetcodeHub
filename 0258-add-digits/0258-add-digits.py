class Solution:
    def addDigits(self, num: int) -> int:
        
        while num >= 10:
            t = 0
            while num:
                t += num % 10 
                num //= 10
            
            num = t
        
        return num
            