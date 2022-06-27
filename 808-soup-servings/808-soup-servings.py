class Solution:
    def soupServings(self, n: int) -> float:
        
        if n > 4800: return 1 
        
        @cache
        def dp(a, b):
            if a <= 0 and b <= 0:
                return 0.5
            elif a <= 0:
                return 1
            elif b <= 0:
                return 0
            
            
            res = 0 
            for x, y in [[4, 0],[3, 1],[2,2], [1,3]]:
                res += dp(a-x, b-y)
            return 0.25 * res 
        n = ceil(n/25)
        return round(dp(n,n), 5)
                
            
            
        