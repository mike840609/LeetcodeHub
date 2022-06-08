# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root: return False
        
        targetSum -= root.val
        
        if not root.left and not root.right:
            return targetSum == 0
        
        l = self.hasPathSum(root.left, targetSum) if root.left else None 
        r = self.hasPathSum(root.right, targetSum) if root.right else None
        return l or r
        
    