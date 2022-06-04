class WordDictionary:

    def __init__(self):
        self.d = {}        

    def addWord(self, word: str) -> None:
        p = self.d
        for w in word:
            if w not in p:
                p[w] = {}
            p = p[w]
        p['#'] = {}

    def search(self, word: str) -> bool:
        
        def dfs(i, p):
            if i == len(word):
                return '#' in p            
            
            if word[i] == '.':
                res = False
                for k in p:
                    res = res or dfs(i+1, p[k])
                return res
            
            elif word[i] in p:
                return dfs(i+1, p[word[i]])
            else:
                return False 
        return dfs(0, self.d)
                
        
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
