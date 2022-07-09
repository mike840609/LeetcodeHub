class Solution:
    def maxCoins(self, A: List[int]) -> int:
        
        A, n = [1] + A + [1], len(A) + 2
        
        dp = [[0] * n for _ in range(n)]
        
        for i in range(n-2, -1, -1):
            for j in range(i+2, n):
                # do not bust A[k] and calculate the left side & right side value
                dp[i][j] = max(A[i]*A[k]*A[j] + dp[i][k] + dp[k][j] for k in range(i + 1, j))
                                
                # for k in range(i+1, j):
                    # print((i, k, j), dp[i][k], dp[k][j])
                    
            # print('------------')
                
        return dp[0][n-1]
        