class TrieNode:
    def __init__(self):
        self.child = defaultdict(TrieNode)
        self.sum = 0
        
class MapSum:

    def __init__(self):
        self.trieRoot = TrieNode()
        self.map = defaultdict(int)

    def insert(self, key: str, val: int) -> None:
        diff = val - self.map[key]
        
        p = self.trieRoot
        for k in key:
            p = p.child[k]
            p.sum += diff
        
        self.map[key] = val
            
                                        
    def sum(self, prefix: str) -> int:
        p = self.trieRoot
                 
        for k in prefix:  
            if k not in p.child: return 0
            p = p.child[k]
        
        return p.sum


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
