class Solution:
    def minimumCost(self, s: str) -> int:
        n = len(s)
        mids = [n//2]
        if n == 0: mids.append(n//2-1)
        
        res = float('inf')
        
        for m in mids:
            cost = 0                         
            invert = False
            for i in range(m+1, n):
                if (s[m] == s[i] and not invert or s[m] != s[i] and invert):
                    continue
                
                cost += n-i
                invert = not invert
                
            invert = False
            for i in range(m-1, -1, -1):                
                if (s[m] == s[i] and not invert or s[m] != s[i] and invert):
                    continue
                    
                cost += i+1
                invert = not invert            
            res = min(res, cost)
                                        
        return res
        
        