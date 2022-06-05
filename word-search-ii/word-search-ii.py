class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        res = set()         
        m, n = len(board), len(board[0])
        maxLen = max([len(w) for w in words])
        
        for word in words:
            p = trie
            for c in word:
                p.setdefault(c, {})
                p = p[c]
            p['$'] = True
        
        
        def dfs(i, j, p, tmp):
            
            if '$' in p :
                res.add(tmp)
            
            if len(tmp) == maxLen:
                return 
                                                            
            for x, y in [(i+1,j), (i-1,j), (i,j+1), (i,j-1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] in p: 
                    c = board[x][y]
                    board[x][y] = '&'
                    dfs(x, y, p[c], tmp+c)
                    board[x][y] = c
        
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    c = board[i][j]
                    board[i][j] = '&'
                    dfs(i, j, trie[c], c)
                    board[i][j] = c
                    
        return list(res)
        