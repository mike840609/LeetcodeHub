class Solution:
    def minPathCost(self, g: List[List[int]], moveCost: List[List[int]]) -> int:
        m, n = len(g), len(g[0])
        dp = [[sys.maxsize] * n for _ in range(m)]
        dp[0] = g[0]
        
        for i in range(m):
            for j in range(n):
                for k in range(n):
                    dp[i][j] = min(dp[i][j], dp[i-1][k] + moveCost[g[i-1][k]][j] + g[i][j])
        
        return min(dp[-1])
    
    