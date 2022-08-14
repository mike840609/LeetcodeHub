class Solution:
    def smallestNumber(self, pattern: str) -> str:
        self.res = []
        
        def dfs(i, s, tmp):
            if self.res:
                return 
            if i >= len(pattern):
                self.res.append(s)
                return
            
            if pattern[i] == 'D':
                for c in tmp:
                    if c < int(s[-1]):
                        tmp.remove(c)
                        dfs(i+1, s+str(c), tmp)
                        tmp.add(c)

                    
            if pattern[i] == 'I':
                for c in tmp:
                    if c > int(s[-1]):
                        tmp.remove(c)
                        dfs(i+1, s+str(c), tmp)
                        tmp.add(c)

        for i in range(1, 10):
            if not self.res :
                s = set([1,2,3,4,5,6,7,8,9])
                s.remove(i)
                dfs(0, str(i), s)
        
        return sorted(self.res)[0]
            
                
                
        
            
                
            
            
            