class Solution:
    def numDecodings(self, s: str) -> int:
        s = ' ' + s
        dp = [0] * len(s) 
        
        dp[0] = 1
        
        for i in range(1, len(s)):      
            
            if 1<= int(s[i]) <= 9:
                dp[i] += dp[i-1]
            
            if 10 <= int(s[i-1] + s[i]) <= 26:
                dp[i] += dp[i-2]
                
        return dp[-1]
            