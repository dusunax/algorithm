# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        temp = ListNode(None, head)
        node = temp

        while node:
            nodes.append(node)
            node = node.next
        
        nodes[-n - 1].next = nodes[-n - 1].next.next

        return temp.next