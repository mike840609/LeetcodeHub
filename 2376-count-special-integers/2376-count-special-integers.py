'''
same as 1012. Numbers With Repeated Digits
'''
class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        L = list(map(int, str(n+1)))
        n = len(L)
        s = set()
        
        res = sum(9 * perm(9, i) for i in range(n-1))
        
        for i, x in enumerate(L):
            for y in range(i==0, x):
                if y not in s:
                    res += perm(9-i, n-i-1)
            
            if x in s:
                break
            s.add(x)
        return res 
            
            
        
        
        

            
                
        
        