class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dp = [[False] * len(heights[0]) for _ in range(len(heights))]
        dp1 = [[False] * len(heights[0]) for _ in range(len(heights))]
        m, n = len(heights), len(heights[0])                
        
        def dfs(i, j, dp):
            if dp[i][j]: return 
            dp[i][j] = True 
            for x, y in [(i+1,j),(i-1,j),(i,j+1),(i,j-1)]:
                if 0 <= x < m and 0 <= y < n and heights[x][y] >= heights[i][j]:
                    dfs(x,y, dp)
                    
        
        for i in range(m):
            dfs(i,0, dp)
            dfs(i,n-1, dp1)
        
        for j in range(n):
            dfs(0,j,dp)
            dfs(m-1,j,dp1)
        
        res = [] 
        for i in range(m):
            for j in range(n):
                if dp[i][j] and dp1[i][j]:
                    res.append([i,j])
        return res 
            
        
            
        
        