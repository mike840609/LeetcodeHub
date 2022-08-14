class Solution:
    def smallestNumber(self, pattern: str) -> str:
        res, stk = [], []        
        for i, val in enumerate(pattern + 'I', 1):
            stk.append(str(i))
            if val == 'I':
                res += stk[::-1]
                stk = [] 
        return ''.join(res)
                
            
                
                
        
            
                
            
            
            