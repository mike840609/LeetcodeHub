class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {} 
    
        maxLen = max([len(w) for w in words])
        for word in words:
            node = trie
            for char in word:
                node = node.setdefault(char, {})
            node['#'] = True

        def search(i, j, node, pre):  
            if '#' in node:  
                res.add(pre)
            
            if len(pre) == maxLen:
                return 
            
            for (x, y) in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n and board[x][y] in node:
                    c = board[x][y]
                    board[x][y] = '&'
                    search(x, y, node[c], pre + c)
                    board[x][y] = c

        res, m, n = set(), len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie:
                    c = board[i][j]
                    board[i][j] = '&'
                    search(i, j, trie[c], c)
                    board[i][j] = c 
        return list(res)