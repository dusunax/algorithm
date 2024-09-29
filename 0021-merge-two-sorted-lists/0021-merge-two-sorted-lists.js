/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
 */
// <Approach 1. Iterative>
// var mergeTwoLists = function(list1, list2) {
//     let temp = new ListNode(-1); // memory
//     let current = temp; // pointer

//     while (list1 !== null && list2 !== null) {
//         if(list1.val < list2.val){
//             current.next = list1;
//             list1 = list1.next;
//         } else {
//             current.next = list2;
//             list2 = list2.next;
//         }
//         current = current.next;
//     }

//     if(list1 !== null){
//         current.next = list1;
//     } else if (list2 !== null) {
//         current.next = list2;
//     }

//     return temp.next;
// };

// <Approach 2: Recursive>
var mergeTwoLists = function(list1, list2) {
    if(list1 === null){
        return list2;
    } else if(list2 === null){
        return list1;
    }
        console.log(list1, list2)

    if(list1.val < list2.val){
        list1.next = mergeTwoLists(list1.next, list2);
        return list1;
    } else {
        list2.next = mergeTwoLists(list1, list2.next);
        return list2;
    }
}