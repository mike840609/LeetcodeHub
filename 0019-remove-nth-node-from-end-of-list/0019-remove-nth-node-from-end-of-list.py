# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        num = 0         
        dummy = p1 = p2 = ListNode()
        dummy.next = head
        
        while p1:            
            p1 = p1.next 
            num += 1
        
        for _ in range(num - n-1):
            p2 = p2.next 
        
        p2.next = p2.next.next 
        return dummy.next