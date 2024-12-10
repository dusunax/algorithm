/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode sortedArrayToBST(int[] nums) {
        return makeBalancedBST(nums);
    }
    public TreeNode makeBalancedBST(int[] nums) {
        if(nums.length == 0) return null;
        int mid = nums.length / 2;
        TreeNode midNode = new TreeNode(nums[mid]);

        int[] leftHalf = Arrays.copyOfRange(nums, 0, mid);
        int[] rightHalf = Arrays.copyOfRange(nums, mid + 1, nums.length);

        midNode.left = makeBalancedBST(leftHalf);
        midNode.right = makeBalancedBST(rightHalf);

        return midNode;
    }
}