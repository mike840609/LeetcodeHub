# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if root:
            return self.dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
        return 0
    
    def dfs(self, root, target):
        if root:
            return int(root.val == target) + self.dfs(root.left, target-root.val) + self.dfs(root.right, target-root.val)
        return 0