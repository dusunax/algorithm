/**
 * // Definition for a Node.
 * function Node(val, next, random) {
 *    this.val = val;
 *    this.next = next;
 *    this.random = random;
 * };
 */

/**
 * @param {Node} head
 * @return {Node}
 */
var copyRandomList = function(head) {
    /** NO set because: need key & value */ 
    /** NO object because: 
     *- don't use same key & value
     *- can set any type for the key 
    */ 
    const visited = new Map();

    const copy = (node) => {
        if (!node) return null;

        // check map!
        if (visited.has(node)) return visited.get(node);

        const newNode = new Node(node.val);
        // key: node, value: newNode
        visited.set(node, newNode);

        // recursive copy
        newNode.next = copy(node.next);
        newNode.random = copy(node.random);

        return newNode;
    };

    return copy(head);
};
