class Solution:
    def rotate(self, A: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(i):
                A[i][j], A[j][i] = A[j][i], A[i][j]
        
        for i in range(m):
            for j in range(n//2):
                A[i][j], A[i][n-j-1] = A[i][n-j-1], A[i][j]
                
                