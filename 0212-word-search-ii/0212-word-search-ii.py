class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        def dfs(i: int, j: int, node: dict, prefix: str):
            letter = board[i][j]
            node = node[letter]
            
            if '$' in node:
                result.append(prefix + letter)
                del node['$']
                
            board[i][j] = '#'
            for r, c in (i+1, j), (i-1, j), (i, j+1), (i, j-1):
                if 0 <= r < m and 0 <= c < n and board[r][c] in node:
                    dfs(r, c, node, prefix + letter)
            board[i][j] = letter

        m, n, result, trie = len(board), len(board[0]), [], {}
        
        for word in words:
            node = trie
            for letter in word:
                node = node.setdefault(letter, {})
            node['$'] = True
            
        for i in range(m):
            for j in range(n):
                if board[i][j] in trie: dfs(i, j, trie, '')
        return result