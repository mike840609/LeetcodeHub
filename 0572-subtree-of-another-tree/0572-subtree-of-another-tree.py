class Solution(object):
    def isSame(self, s, t):
        if not s and not t : return True         
        if s and t:
            return s.val == t.val and self.isSame(s.left, t.left) and self.isSame(s.right, t.right)
        return False 
    
    def isSubtree(self, s, t):        
        if self.isSame(s,t): return True
        if not s: return False 
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        
            
        
        
                
        
        