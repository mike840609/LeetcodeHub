class Solution:
    def distinctSequences(self, n: int) -> int:
        
        m = [[1,2,3,4,5,6], 
             [2,3,4,5,6],
             [1,3,5],
             [1,2,4,5],
             [1,3,5],
             [1,2,3,4,6],
             [1,5]]
        
        @lru_cache(None)
        def dfs(n, ppre, pre):
            if n == 0:
                return 1
            
            tmp = 0
            for x in m[pre]:
                if x != ppre:
                    tmp += dfs(n-1, pre, x)
            return tmp
        
        return dfs(n, 0, 0) % (10**9 + 7) 