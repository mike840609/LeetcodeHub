class Solution:
    def longestPalindrome(self, s: str) -> str:
        m = len(s)
        dp = [[0] * m for _ in range(m)] 
        res = s[0]
        
        for i in range(m-1, -1, -1):
            for j in range(m-1, i-1, -1):
                if i == j:
                    dp[i][j] = 1
                    
                elif s[i] == s[j] and (j - i == 1 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1
                    if j+1 - i + 1 > len(res):
                        res = s[i:j+1]
        # for l in dp:
        #     print(l)
            
        return res 
                    