class Solution:
    def numSquares(self, n: int) -> int:
        if n < 2 : return n 

        l = [x**2 for x in range(1,int(n**0.5)+1)]
        
        q = [n]
        res = 0 
        while q:
            tmp = []
            for n in q:                
                for x in l:
                    if n-x > 0:
                        tmp.append(n-x)
                    elif n == x:
                        return res+1
            res += 1
            q = tmp
        return -1
                        
                    
                
        