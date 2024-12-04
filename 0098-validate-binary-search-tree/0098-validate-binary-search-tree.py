# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        min = float("-inf")
        max = float("inf")
        
        def bstCheck(self, node, min, max) -> bool:
            if not node:
                return True 
            if node.val <= min or node.val >= max:
                return False
            
            return bstCheck(self, node.left, min, node.val) and bstCheck(self, node.right, node.val, max)

        return bstCheck(self, root, min, max)
                
        
        
        