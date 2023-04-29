# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.res = [] 
        
        def dfs(root, s, p):
            if not root: return                 
            if not root.left and not root.right:
                if s == root.val:                    
                    self.res.append(p + [root.val])
                return 
        
            
            dfs(root.left, s-root.val, p + [root.val])
            dfs(root.right, s-root.val, p + [root.val] )
        
        dfs(root, targetSum, [])
        return self.res
        