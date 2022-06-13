class Solution(object):
    def minPathSum(self, grid):
        mem = {}
        return self.f(len(grid) - 1, len(grid[0]) - 1, grid, mem)
        
    def f(self,i,j,grid,mem):
        if (i, j) not in mem:
            mem[(i, j)] = grid[i][j] + min([self.f(i, j - 1, grid, mem) if (j - 1 >= 0) else float('inf'), 
                                            self.f(i - 1, j, grid, mem) if (i - 1 >= 0) else float('inf'),
                                            0 if i==0 and j == 0 else float('inf')])
        return mem[(i, j)]