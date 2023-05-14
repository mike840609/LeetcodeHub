class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        res = [] 
        d = set(wordDict)
        
        @lru_cache(None)
        def dfs(s, tmp):
            if not s:
                res.append(tmp.strip())
                return 
            
            for i in range(len(s)+1):
                if s[:i] in d:
                    dfs(s[i:], tmp + " " + s[:i])
        dfs(s, '')
        return res