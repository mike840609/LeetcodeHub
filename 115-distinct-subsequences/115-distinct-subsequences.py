class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t)+1, len(s)+1
        dp = [[0] * n for _ in range(m)] 
        
        for i in range(n):
            dp[0][i] = 1
        
        
        
        for i in range(m-1):
            for j in range(n-1):
                if t[i] == s[j]:
                    dp[i+1][j+1] = dp[i][j] + dp[i+1][j]
                
                else:
                    dp[i+1][j+1] = dp[i+1][j]
        
        
#         for l in dp :
#             print(l)
        
        return dp[-1][-1]
            
            