class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        
        @lru_cache(None)
        def dfs(t, n):
            if n == 0 :  
                if t == 0:
                    return 1 
                return 0
            
            res = 0 
            for i in range(1, k+1):
                res += dfs(t-i, n-1)            
            return res % (10**9+7)
    
        return dfs(target, n) % (10**9+7)