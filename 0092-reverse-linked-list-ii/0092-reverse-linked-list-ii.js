/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} left
 * @param {number} right
 * @return {ListNode}
 */
const reverseBetween = (list, left, right) => {
    // temp node = head
    const temp = new ListNode(0, list);
    let head = temp;
    let curr = 1;

    // move until left index
    while (curr++ < left) head = head.next;

    // tail => be first node
    let tail = head.next;
    while (left++ < right) {
        const nextNode = tail.next; // tail의 다음 노드
        tail.next = nextNode.next; // tail의 다음 노드를 다다음노드로~ 쭉쭉
        
        nextNode.next = head.next; // 뒤집기
        head.next = nextNode;
    }
    return temp.next;
};