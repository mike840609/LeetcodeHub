"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node):
            if node and node not in clone:
                clone[node] = Node(node.val, [])
                clone[node].neighbors = [dfs(nei) for nei in node.neighbors]
            return clone.get(node)
        
        clone = {}
        return dfs(node)