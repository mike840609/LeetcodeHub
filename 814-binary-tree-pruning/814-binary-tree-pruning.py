# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root.left and not root.right and root.val == 0:
            return None
        
        l = self.pruneTree(root.left) if root.left else None
        r = self.pruneTree(root.right) if root.right else None
        
        if not l and not r and root.val == 0 :
            return None
        
        root.left = l 
        root.right = r 
        return root
        
        
        