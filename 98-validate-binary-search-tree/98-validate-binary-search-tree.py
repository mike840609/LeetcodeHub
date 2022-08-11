# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:    
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(min_, max_, root):
            if not root:
                return True 
            
            l = dfs(min_, root.val, root.left)
            r = dfs(root.val, max_, root.right)
            if min_ < root.val < max_:
                return l and r 
            else:
                return False 
        return dfs(float('-inf'), float('inf'), root)
            
        