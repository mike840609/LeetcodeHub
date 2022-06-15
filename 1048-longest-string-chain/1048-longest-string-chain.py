class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        self.res = 0 
        words.sort(key=len)
        dp = Counter()
        
        for w in words:
            
            dp.setdefault(w, 1)
            
            for i in range(len(w)):
                k = w[:i]+w[i+1:]
                if k in dp:
                    dp[w] = max(dp[w], dp[k]+1)
                    
        return max(dp.values())
            
                    
                
                    
                