class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        s = set(arr)
        N = (10**9+7)
        
        @lru_cache(None)
        def dp(n):
            ans = 1 
            for cand in s:
                if n % cand == 0 and n//cand in s:
                    ans += dp(cand) *dp(n//cand)
            return ans 
        
        return sum(dp(n) for n in s) % N
            
        