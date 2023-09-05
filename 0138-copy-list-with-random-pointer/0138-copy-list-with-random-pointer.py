"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        d = {}
        
        p = head
        
        while p:
            n = p.next
            r = p.random            
            if p not in d:
                d[p] = Node(p.val)
            
            if n:
                if n not in d:
                    d[n] = Node(n.val)                            
                d[p].next = d[n]
                             
            if r:
                if r not in d:
                    d[r] = Node(r.val)                
                d[p].random = d[r]
            
            p = p.next
        
        return d[head] if head in d else head 
            
            
            
                
            
            
        