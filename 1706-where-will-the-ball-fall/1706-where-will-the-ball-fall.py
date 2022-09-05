class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            nonlocal n
            nonlocal m
                        
            if j == 0 and grid[i][j] == -1:
                return -1 
            
            if j == n-1 and grid[i][j] == 1:
                return -1
            
            if grid[i][j] == 1 and grid[i][j+1] == -1:
                return -1
            
            if grid[i][j] == -1 and grid[i][j-1] == 1:
                return -1            
            
            if i == m-1:
                return j + grid[i][j]
            
            return dfs(i+1, j + grid[i][j])
        
        res = []
        
        for j in range(n):
            res.append(dfs(0,j))
        return res 
        
            
            
            
            