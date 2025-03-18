# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''

- left is smaller than val
- right is bigger than val
'''
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low = float('-inf'), high = float('inf')):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        
        return dfs(root) 

'''
- 루트와의 비교를 수행하지 않았음
- failed testcase: [5,4,6,null,null,3,7]
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node): # this'll only compared with its immediate left and right children.
            if not node:
                return True
            if node.left and node.val <= node.left.val:
                return False
            if node.right and node.val >= node.right.val:
                return False
            
            return dfs(node.left) and dfs(node.right)
        
        return dfs(root) 
'''