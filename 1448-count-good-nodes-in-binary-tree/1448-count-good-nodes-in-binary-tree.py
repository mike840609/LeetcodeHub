# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 0 
        
        def dfs(biggest, root):
            nonlocal res 
            
            if not root : return 
            if root.val >= biggest:
                res += 1
                
            
            dfs(max(biggest, root.val), root.left)
            dfs(max(biggest, root.val), root.right)
        
        dfs(root.val, root)
        return res 
                