class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        dp = [[float(inf)] * (n+1) for _ in range(m+1)] 
        
        dp[-1][-2] = 1
        dp[-2][-1] = 1
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                dp[i][j] = max(min(dp[i+1][j], dp[i][j+1])- dungeon[i][j], 1)
        
        # for l in dp :
            # print(l)
            
        return dp[0][0]