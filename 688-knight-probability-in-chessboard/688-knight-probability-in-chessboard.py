class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:        

        pos = [[-1, -2], [-1, +2], [-2, -1], [-2, 1], [1, -2], [1, +2], [2, -1], [2, +1]]                
                
        @lru_cache(None)
        def dp(i, j, k):                        
            
            if k == 0 :
                return 1
                        
            cnt = 0
            for x, y in pos:
                if 0 <= i+x < n and 0 <= j+y < n :
                    cnt += dp(i+x, j+y, k-1)                                                                                    
            return cnt                 
                    
        return dp(row, column, k) / (8**k)
                    
            