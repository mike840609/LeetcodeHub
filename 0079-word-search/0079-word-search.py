class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        dp = [[0] * n for _ in range(m)]
        self.res = False 
        
        def dfs(i, j, idx):
            if idx == len(word)-1 and word[idx] == board[i][j]:
                self.res = True 
                return 
            
            if self.res == True:
                return 
            
            if board[i][j] != word[idx]: 
                return
            
            for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if 0 <= x < m and 0 <= y < n and dp[x][y] == False:                    
                    dp[x][y] = True 
                    dfs(x, y, idx+1)
                    dp[x][y] = False
        
        for i in range(m):
            for j in range(n):
                dp[i][j] = True 
                dfs(i,j, 0)
                dp[i][j] = False
        
        return self.res
                    
            
        