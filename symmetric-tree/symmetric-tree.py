# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def swap(root):
            if not root : return 
            
            root.left, root.right = swap(root.right), swap(root.left)
            return root
        
        def compare(r1, r2):
            if not r1 and not r2:
                return True 
            if r1 and r2:
                r, l = compare(r1.right, r2.right), compare(r1.left, r2.left)
                return r1.val == r2.val and r and l
            return False
                    
        
        root.left = swap(root.left)
        return compare(root.right, root.left)
        