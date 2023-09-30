class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        # 231 from right to left 
        stk = []         
        s = -float('inf')
        
        for n in nums[::-1]:
            if not stk:
                stk.append(n)
            
            if n < s:
                return True 
            
            while stk and stk[-1] < n :
                s = stk.pop()
            
            stk.append(n)
        
        return False 
        
        
        
        
        