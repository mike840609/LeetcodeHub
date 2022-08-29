class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            if grid[i][j] == '-1':
                return 
            
            grid[i][j] = '-1'
            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= x < m and 0<= y < n and grid[x][y] == '1':
                    dfs(x,y)
        
        res = 0 
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    res += 1
                    dfs(i,j)
        return res 
                    