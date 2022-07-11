class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        m, n = len(s1), len(s2)
        
        dp = [[0] * (n+1) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):                
                if s1[i] == s2[j]:
                    dp[i+1][j+1] = dp[i][j] + ord(s2[j])
                else:
                    if dp[i][j+1] >= dp[i+1][j]:
                        dp[i+1][j+1] = dp[i][j+1] 
                    else:
                        dp[i+1][j+1] = dp[i+1][j]        
                 
        res = sum([ord(x) for x in s1]) + sum([ord(x) for x in s2])                
        return res - 2*dp[-1][-1]
            
            
                
                    