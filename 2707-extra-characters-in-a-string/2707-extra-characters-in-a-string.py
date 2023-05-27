class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:        
        
        @lru_cache(None)
        def dfs(i, extra):
            if i == len(s):
                return extra
            
            min_extra = dfs(i+1, extra)
            
            for w in dictionary:
                if s[i:].startswith(w):
                    min_extra = min(min_extra, dfs(i+len(w), extra-len(w)))
            
            return min_extra
            
            
                
        
        
        return dfs(0, len(s))
                
        