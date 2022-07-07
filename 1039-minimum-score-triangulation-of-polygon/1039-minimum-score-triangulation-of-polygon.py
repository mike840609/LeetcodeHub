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
        
        ## bottom up 
        n = len(A)
        dp = [[0] *n for i in range(n)]
        
        for i in range(2, n):
            for l in range(0, n-i):
                r = l+i
                dp[l][r] = float('inf')
                for k in range(l+1, r):
                    dp[l][r] = min(dp[l][r], dp[l][k] + dp[k][r] + A[l]*A[r]*A[k])
        
        return dp[0][-1]
                
                
                