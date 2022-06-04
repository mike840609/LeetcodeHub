class Trie:

    def __init__(self):
        self.d = {}        

    def insert(self, word: str) -> None:
        p = self.d
        for w in word:
            if w not in p:
                p[w] = {}            
            p = p[w]
        
        p['#'] = {}
        

    def search(self, word: str) -> bool:
        p = self.d
        for w in word:
            if w in p:
                p = p[w]
            else:
                return False 
        return "#" in p
        

    def startsWith(self, prefix: str) -> bool:
        p = self.d
        for w in prefix:
            if w in p:
                p = p[w]
            else:
                return False
        return True 
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)