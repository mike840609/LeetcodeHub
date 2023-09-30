class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # 231 from right to left 
    
        # increase monotonic stack 
        stk, third = [], float('-inf')        
        
        for n in nums[::-1]:            
            if n < third:
                return True             
            while stk and stk[-1] < n :
                third = stk.pop()            
            stk.append(n)        
        return False                                 
        