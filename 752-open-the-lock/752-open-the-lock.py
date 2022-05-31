class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends: return -1
        
        q = [(0,0,0,0)] 
        target = tuple([int(x) for x in target])
        
        s2 = set()
        for l in deadends:            
            s2.add(tuple(int(x) for x in l))
    
        res = 0 
        seen = set()
        
        
        while q:
            tmp = []        
            for l in q:
                if l == target:                    
                    return res                 
                w,x,y,z = l                
                t1 = ((w+1)%10,x,y,z)
                t2 = ((w-1+10)%10,x,y,z)
                t3 = (w,(x+1)%10,y,z)
                t4 = (w,(x-1+10)%10,y,z)
                t5 = (w,x,(y+1)%10,z)
                t6 = (w,x,(y-1+10)%10,z)
                t7 = (w,x,y,(z+1)%10)
                t8 = (w,x,y,(z-1+10)%10)
                
                for t in [t1,t2,t3,t4,t5,t6,t7,t8]:
                    if t not in seen and t not in s2:
                        seen.add(t)
                        tmp.append(t)            
            q = tmp                            
            res += 1
            
        return -1
                
                
            