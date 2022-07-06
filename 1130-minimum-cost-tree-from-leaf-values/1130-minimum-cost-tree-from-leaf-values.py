class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        
        @lru_cache(None)
        def dp(i, j):
            if j <= i :
                return 0
            
            res = float('inf')
            for k in range(i+1, j+1):
                res = min(res, dp(i, k-1) + dp(k, j) + max(arr[i:k]) * max(arr[k:j+1]))            
            return res 
        
        return dp(0, len(arr)-1)
                