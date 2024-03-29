# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder: return None
        
        root = TreeNode(preorder.pop(0))
        idx = inorder.index(root.val)
        
        root.left = self.buildTree(preorder[:idx], inorder[:idx])
        root.right = self.buildTree(preorder[idx:], inorder[idx+1:])
        
        return root
        
        