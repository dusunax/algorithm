# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # <Approach 1. Iterative>
    # def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    #     temp = ListNode(-1)
    #     current = temp

    #     while list1 is not None and list2 is not None:
    #         if list1.val < list2.val:
    #             current.next = list1
    #             list1 = list1.next
    #         else:
    #             current.next = list2
    #             list2 = list2.next
    #         current = current.next
        
    #     if list1 is not None:
    #         current.next = list1
    #     elif list2 is not None:
    #         current.next = list2

    #     return temp.next

    # <Approach 2: Recursive>
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        elif list2 is None:
            return list1

        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2
    
# \U0001f449 NameError: name 'mergeTwoLists' is not defined
# Error occurs because you're trying to call the mergeTwoLists method from within itself without referencing it. 
# In Python, when you call a method from within another method of the same class, you need to use self to refer to the instance of the class.