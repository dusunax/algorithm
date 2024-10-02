/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 */
var isPalindrome = function(head) {
    if (!head || !head.next) return true;

    let slow = head;
    let fast = head;
    while (fast && fast.next) {
        slow = slow.next; // move 1 node
        fast = fast.next.next; // move 2 node
    }

    let prev = null;
    // reversing the second half of the list
    while (slow) {
        let nextNode = slow.next; 
        slow.next = prev;
        prev = slow;
        slow = nextNode;
    }

    let left = head;
    let right = prev;
    while (right) {
        if (left.val !== right.val) {
            return false;
        }
        left = left.next;
        right = right.next;
    }

    return true;
};