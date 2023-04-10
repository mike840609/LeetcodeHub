# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def flip(root):
            if not root: return             
            root.left, root.right = flip(root.right), flip(root.left)
            return root
        
        def compare(r1, r2):
            if not r1 and not r2:
                return True
            if r1 and r2:
                l = compare(r1.left, r2.left)
                r = compare(r1.right, r2.right)
                return l and r and r1.val == r2.val
            return False
        
        
        flip(root.left)
        return compare(root.left, root.right)
            