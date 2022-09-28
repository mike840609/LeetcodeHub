# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        pre = dummy 
        cur = dummy 
        
        for _ in range(n+1):
            cur = cur.next 
        
        while cur:             
            cur = cur.next
            pre = pre.next
        
        pre.next = pre.next.next 
        return dummy.next