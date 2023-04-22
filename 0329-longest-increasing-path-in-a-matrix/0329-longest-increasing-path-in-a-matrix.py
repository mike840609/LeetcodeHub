class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        m, n = len(matrix), len(matrix[0])
        
        dp = [[1] * n for _ in range(m)]
        
        
        def dfs(i, j):
            if dp[i][j] != 1:
                return dp[i][j]
                        
            
            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:                    
                    dp[i][j] = max(dp[i][j], dfs(x,y)+1)
            
            return dp[i][j]
        
        
        for i in range(m):
            for j in range(n):
                dfs(i, j)
        
        # print(dp)
        
        l = [ x for sub in dp for x in sub]
        return max(l)
                
            
            
            
        
        