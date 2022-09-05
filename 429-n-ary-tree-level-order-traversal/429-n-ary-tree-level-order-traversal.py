"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root : return []
        
        res = []
        q = deque([root])
        
        while q:
            tmpRes = [] 
            for _ in range(len(q)):
                node = q.popleft()
                q += node.children            
                tmpRes += [node.val]
            res.append(tmpRes)
            
        return res 
                    
            
        
        