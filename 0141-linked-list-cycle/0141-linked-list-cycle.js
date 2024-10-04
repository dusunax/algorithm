/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

/**
 * @param {ListNode} head
 * @return {boolean}
 */
var hasCycle = function(head) {
    if(!head || !head.next) {
        return false;
    }

    let slow = head;
    let fast = head;

    // Floyd's Tortoise and Hare
    // cycle이 있을 때 두 포인터가 언젠가 반드시 만난다
    while (slow !== fast) {
        if(!fast || fast.next){
            return false;
        }
        slow = slow.next;
        fast = fast.next.next;
    }

    return true;
};