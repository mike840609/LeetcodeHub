class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        trie = {}
        
        for word in words:
            p = trie
            for c in word[::-1]:
                p.setdefault(c, {})
                p = p[c]            
        
        
        self.res = 0        
        def dfs(root, i):
            if not root:
                self.res += (i+1)
                return 
                
            for k, v in root.items():
                dfs(v, i+1)
        
        dfs(trie, 0)
        return self.res 
                