# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSame(self, r1, r2):
        if not r1 and not r2:
            return True 
        if r1 and r2:
            return r1.val == r2.val and self.isSame(r1.left, r2.left) and self.isSame(r1.right, r2.right)            
        return False 
    
    def isSubtree(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> bool:
        if self.isSame(r1,r2):
            return True 
        if not r1:
            return False 
        return self.isSubtree(r1.left, r2) or self.isSubtree(r1.right, r2)
        