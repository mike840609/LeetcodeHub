class Solution:
    def uniquePathsWithObstacles(self, A: List[List[int]]) -> int:
        if A[0][0] == 1: return 0
        
        m, n = len(A), len(A[0])
        for i in range(m):
            for j in range(n):
                A[i][j] = 1-A[i][j]                                                                               
        
        for i in range(m):
            for j in range(n):
                
                if (i ==0 and j == 0) or A[i][j] == 0:
                    continue
                    
                if i == 0:
                    A[i][j] = A[0][j-1]
                elif j == 0:
                    A[i][j] = A[i-1][0]
                else:
                    A[i][j] = A[i-1][j] + A[i][j-1]
        
        return A[-1][-1]