class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            res = 0
            if grid[i][j] == 1:
                grid[i][j] = 0                
                res = 1
                for x, y in [(i, j-1), (i-1, j), (i,j+1), (i+1, j)]:
                    if 0 <= x < m and 0 <= y < n:
                        res += dfs(x, y)
            return res
        
                        
        res = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]:                    
                    res = max(dfs(i, j), res)
        return res
                    