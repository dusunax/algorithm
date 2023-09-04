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
    if (!head || !head.next) return false;

    let before = head;
    let forward = head.next;

    while (before !== forward) {
        if (!forward || !forward.next) return false;
        
        before = before.next;
        forward = forward.next.next;
    }

    return true;
};