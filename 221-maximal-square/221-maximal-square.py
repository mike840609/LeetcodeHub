class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        
        for i in range(m):
            for j in range(n):
                matrix[i][j] = int(matrix[i][j])
        res = 0
        for i in range(m):
            for j in range(n):                
                if matrix[i][j]:
                    a = matrix[i-1][j-1] if i-1 >= 0 and j-1 >=0 else 0
                    b = matrix[i-1][j] if i-1 >= 0 else 0
                    c = matrix[i][j-1] if j-1 >= 0 else 0
                    matrix[i][j] = min([a, b, c]) + 1 
                    res = max(res, matrix[i][j])
        
        return res ** 2