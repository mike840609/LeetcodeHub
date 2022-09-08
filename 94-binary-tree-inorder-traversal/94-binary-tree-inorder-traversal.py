# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root : return [] 
        
        stk = [root] 
        res = [] 
        while stk:            
            node = stk.pop()
            if node.left:
                stk.append(node)
                stk.append(node.left)                
                node.left = None                
            
            else:                
                res.append(node.val)                
            
                if node.right:
                    stk.append(node.right)
                
        return res