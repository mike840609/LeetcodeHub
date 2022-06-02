# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        
        stk = [root] 
        res = [] 
        
        while stk:            
            node = stk.pop()
            if node and node.left:
                left = node.left
                node.left = None
                stk.append(node)
                stk.append(left)                
            else:                
                res.append(node.val) 
                if node.right:
                    stk.append(node.right)
        return res
                
                