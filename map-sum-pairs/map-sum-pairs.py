class MapSum:

    def __init__(self):
        self.d = {}                

    def insert(self, key: str, val: int) -> None:
        p = self.d
        for k in key:            
            if k not in p:
                p[k] = {}                
                
            p = p[k]
            
            if 'val' not in p:
                p['val'] = {}
                
            p['val'][key] = val 
                    
                    

    def sum(self, prefix: str) -> int:
        p = self.d
                 
        for k in prefix:
            if k not in p :
                return 0        
            p = p[k]
        
        return sum([val for _, val in p['val'].items()])


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)