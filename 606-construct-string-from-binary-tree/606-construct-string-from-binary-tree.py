# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        l = self.tree2str(root.left)
        r = self.tree2str(root.right)
        
        res = str(root.val)
        if l:
            res += '(' + l +')'         
        if r :
            if not l:
                res += '()(' + r +')'
            else:
                res += '(' + r +')'
        return  res 
    
        
            