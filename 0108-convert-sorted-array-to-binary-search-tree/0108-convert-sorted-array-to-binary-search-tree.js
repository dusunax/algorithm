/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    const makeBalancedBST = (nums) => {
        if(!nums.length) return null;
        const mid = Math.floor(nums.length / 2);
        const midNode = new TreeNode(nums[mid]);
        
        midNode.left = makeBalancedBST(nums.slice(0, mid));
        midNode.right = makeBalancedBST(nums.slice(mid + 1));

        return midNode
    }
    return makeBalancedBST(nums)
};