class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        
        for i in range(m):
            for j in range(n):
                if mat[i][j] != 0 :
                    top = mat[i-1][j] if i-1 >= 0 else float('inf')
                    left = mat[i][j-1] if j-1 >= 0 else float('inf')
                    mat[i][j] = min(top , left) + 1
        
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                down = mat[i+1][j] if i+1 < m else float('inf')
                right  = mat[i][j+1] if j+1 < n else float('inf')
                mat[i][j] = min(mat[i][j], down + 1, right + 1)
                
        return mat
                
                