# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        j = k = dummy 
        
        
        for _ in range(n):
            j = j.next 
        
        while j.next:
            j = j.next             
            k = k.next 
        k.next = k.next.next 
        return dummy.next
    
            
        