class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j))
    
        # print(q)
        res = -1
        while q:
            res += 1
            
            for _ in range(len(q)):
                i, j = q.popleft()
                for x,y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                        grid[x][y] = 2
                        q.append((x,y))
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return -1
        return max(res, 0)
                        
                
                
        
        
        
        
            