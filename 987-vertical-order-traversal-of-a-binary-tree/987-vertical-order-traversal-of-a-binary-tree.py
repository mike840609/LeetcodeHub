# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        d = defaultdict(list)
        
        q = deque([(root, 0)])
        
        while q:
            tmp = defaultdict(list)
            for _ in range(len(q)):
                node, j = q.popleft()
                
                if node.left:
                    q.append([node.left, j-1])
                if node.right:
                    q.append([node.right, j+1])
                
                tmp[j].append(node.val)
            
            for j, v in tmp.items():
                d[j] += sorted(v)
        
        res = []
        for k in sorted(d.keys()):
            res.append(d[k])
        
        return res
    
                
            