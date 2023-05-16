# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head 
        p = dummy 
        while p.next and p.next.next:
            n3 = p.next.next.next
            n1 = p.next
            n2 = p.next.next
            p.next = n2
            n2.next = n1
            n1.next = n3
            p = p.next.next 
        
        return dummy.next
            
        