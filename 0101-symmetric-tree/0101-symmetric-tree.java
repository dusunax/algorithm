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
    public boolean isSymmetric(TreeNode root) {
        return chkSymmetric(root.left, root.right);
    }
    public boolean chkSymmetric(TreeNode leftSide, TreeNode rightSide) {
        if (leftSide == null || rightSide == null) {
            return leftSide == rightSide;
        }
        if (leftSide.val != rightSide.val) {
            return false;
        }
        
        return chkSymmetric(leftSide.left, rightSide.right) && chkSymmetric(leftSide.right, rightSide.left);
    }
}