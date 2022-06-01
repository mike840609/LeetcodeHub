class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2 : return n 

        # tip: use int(n**0.5)+1 as end, because we want to consider int(n**0.5),
        # so add 1 to make sure we take int(n**0.5)
        l = [x**2 for x in range(1,int(n**0.5)+1)]
        
        q = set([n])
        res = 0 
        
        while q:
            res += 1
            tmp = set()
            for n in q:                
                for x in l:
                    if n-x > 0:
                        tmp.add(n-x)
                    elif n == x:
                        return res            
            q = tmp
        return -1
                        
                    
                
        