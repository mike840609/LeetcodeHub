class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        s = " " + s
        dp = [0] * len(s)
        dic = set(wordDict)
        dp[0] = 1 
        
        for i in range(len(s)+1):
            for w in dic:
                if i >= len(w) and dp[i-len(w)-1] and s[i-len(w):i] == w:                
                    dp[i-1] = True                        
        
        return dp[-1]