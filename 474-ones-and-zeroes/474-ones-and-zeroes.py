class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] *(n+1) for _ in range(m+1)]
        
        for s in strs:
            zeros, ones = s.count('0'), s.count('1')
            
            ## WATCH OUT FOR LOOPS,
            ## 1. We are traversing reverse to prevent sub problem overlapping,(若從 zeros -> m 則會不斷重複計算)  
            # consider string "01" and m = 5, n = 3 and draw matrix from normal order and in reverse order, you'll understand
            ## 2. The lower limit is number of zeros and ones, coz before that you wont find any match
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones] + 1)
        return dp[-1][-1]