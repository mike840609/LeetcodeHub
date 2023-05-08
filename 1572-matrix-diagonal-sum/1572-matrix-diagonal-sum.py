class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        res = 0 
        m = len(mat)
        j = 0 
        for i in range(m):
            res += mat[i][j] + mat[i][m-j-1]
            j += 1
        
        if m%2 :
            res -= mat[m//2][m//2]
        
        return res