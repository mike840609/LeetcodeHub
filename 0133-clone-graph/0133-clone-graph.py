"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        q = deque()
        d = {}
        
        if node:
            q.append(node)
                    
        
        while q:
            n = q.popleft()
            if n not in d:
                d[n] = Node(n.val)
            
            l = []
            for adj in n.neighbors:
                if adj not in d:
                    d[adj] = Node(adj.val)
                    q.append(adj)
                l.append(d[adj])
            
            d[n].neighbors = l
        
        return d.get(node, None)
                