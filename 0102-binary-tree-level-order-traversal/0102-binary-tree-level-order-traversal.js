/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var levelOrder = function(root) {
    const result = [];

    const traverse = (node, level) => {
        if(!node) return;
        if(result.length <= level){
            result.push([])
        }

        result[level].push(node.val);
        
        node.left && traverse(node.left, level + 1);
        node.right && traverse(node.right, level + 1);
    }

    traverse(root, 0)
    return result;
};