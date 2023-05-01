class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if n == 0 : return len(tasks)
        cnt = Counter(tasks)
        h = []
        for k, v in cnt.items():
            heappush(h, (-v, k))
        
        res = 0 
        while h:
            t = [] 
            
            for i in range(n+1):    
                res += 1
                if h:                    
                    v, k = heappop(h)                
                    v += 1                                    
                    if v != 0 :
                        t.append((v, k))                                    
            
                if not t and not h :                
                    return res 
                    
            for x, y in t:
                heappush(h, (x, y))                        
            
            
        
        return res
                