'''
Intuition
    The connected two points in polygon shares one common edge,
    these two points must be one and only one triangles.


Explanation
    dp[i][j] means the minimum score to triangulate A[i] ~ A[j],
    while there is edge connect A[i] and A[j].

We enumerate all points A[k] with i < k < j to form a triangle.

The score of this triangulation is dp[i][j], dp[i][k] + dp[k][j] + A[i] * A[j] * A[k]

'''

class Solution:
    def minScoreTriangulation(self, A: List[int]) -> int:
        
        ## top down
        @lru_cache(None)
        def dp(i, j):
            if j-i == 2:
                return A[i] * A[i+1] *A[i+2]
            
            if j-i < 2 :
                return 0
            
            res = float('inf')
            
            for k in range(i+1, j):
                res = min(res, dp(i, k) + dp(k, j) + A[i] * A[k] * A[j])
            
            return res
        
        return dp(0, len(A)-1)
                
                
                