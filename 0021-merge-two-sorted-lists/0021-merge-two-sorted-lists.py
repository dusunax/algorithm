# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # <Approach 1. Iterative>
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(-1)
        current = temp

        while list1 is not None and list2 is not None:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        if list1 is not None:
            current.next = list1
        elif list2 is not None:
            current.next = list2

        return temp.next


#         // var mergeTwoLists = function(list1, list2) {
# //     let temp = new ListNode(-1); // memory
# //     let current = temp; // pointer

# //     while (list1 !== null && list2 !== null) {
# //         if(list1.val < list2.val){
# //             current.next = list1;
# //             list1 = list1.next;
# //         } else {
# //             current.next = list2;
# //             list2 = list2.next;
# //         }
# //         current = current.next;
# //     }

# //     if(list1 !== null){
# //         current.next = list1;
# //     } else if (list2 !== null) {
# //         current.next = list2;
# //     }

# //     return temp.next;
# // };

# // 재귀
# var mergeTwoLists = function(list1, list2) {
#     if(list1 === null){
#         return list2;
#     } else if(list2 === null){
#         return list1;
#     }
#         console.log(list1, list2)

#     if(list1.val < list2.val){
#         list1.next = mergeTwoLists(list1.next, list2);
#         return list1;
#     } else {
#         list2.next = mergeTwoLists(list1, list2.next);
#         return list2;
#     }
# }