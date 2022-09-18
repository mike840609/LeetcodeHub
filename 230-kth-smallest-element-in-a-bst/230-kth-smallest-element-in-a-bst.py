# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:                
        
        def pushLeft(stk, root):
            while root:
                stk.append(root)
                root = root.left
        
        
        stk = []
        pushLeft(stk, root)
        
        while k  > 1:            
            pushLeft(stk, stk.pop().right)
            k -= 1
            
        return stk.pop().val
        
        
            

    
        
        
            