'''
- separate odd/even indices
- reorder by odd-even 
- it's stable (no mixed up of relative order) 
- TC should be O(1): have to manipulate the order as you go
- SC is also should be O(1): no extra structure. just re-linking nodes
- i is starts from 1
'''
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        if head.next is None or head.next.next is None:
            return head

        even_head = head.next
        odd = head
        even = head.next
        
        while even is not None and even.next is not None:
            odd.next = even.next
            odd = odd.next

            even.next = odd.next
            even = even.next

        odd.next = even_head

        return head 