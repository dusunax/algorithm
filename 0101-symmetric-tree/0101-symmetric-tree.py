# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def chkSymmetric(leftSide, rightSide):
            if leftSide is None and rightSide is None:
                return True
            if leftSide is None or rightSide is None:
                return False
            if leftSide.val != rightSide.val:
                return False

            return chkSymmetric(leftSide.left, rightSide.right) and chkSymmetric(leftSide.right, rightSide.left)
        
        return chkSymmetric(root.left, root.right)