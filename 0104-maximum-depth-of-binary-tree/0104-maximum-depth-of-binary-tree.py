# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int: 
        max_depth = 0

        def helper(node, count):
            nonlocal max_depth 
            if node is None:
                max_depth = max(max_depth, count)
                return

            helper(node.left, count+1) 
            helper(node.right, count + 1)

        helper(root, max_depth)

        return max_depth
                