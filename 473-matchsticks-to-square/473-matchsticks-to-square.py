class Solution:
    def makesquare(self, A: List[int]) -> bool:
                
        @lru_cache(None)
        def dp(mask, cur):
            if mask == 0 : return cur == target 
            
            if cur == target: return dp(mask, 0)
            
            for i in range(len(A)):
                
                if cur + A[i] > target:
                    break
                    
                if (mask & (1 << i)) > 0 and dp(mask ^ (1<<i), cur + A[i]):
                    return True 
                
            return False 
        
        target, rest = divmod(sum(A), 4)        
        if rest > 0: return False
        A.sort()        
        return dp(2**len(A)-1, 0)
            
            
                