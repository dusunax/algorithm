'''
- separate odd/even indices
- reorder by odd-even 
- it's stable (no mixed up of relative order) 
- TC should be O(n): have to manipulate the order as you go
- SC is also should be O(1): no extra structure. just re-linking nodes
- i is starts from 1
'''
 
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    # Linked-list
    - TC is O(n), travarse once
    - SC is O(1), no additional structure
    '''
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
            '''
            # Always move odd first, then even — avoids extra temp variables 
            \U0001f449 move the odd first to simplify the pointer jumping and etc. 
            Like `even = even.next.next` or use addition temp variable.
            '''
            even.next = odd.next 
            even = even.next

        odd.next = even_head

        return head 