# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
# DFS 
'''
# 
class Solution:
    '''
    TC: O(n), 모든 노드 방문
    SC: O(h), 편향 트리 O(h), 균형 시 O(log n), n=h
    '''
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [(root, 1)] 
        max_depth = 0

        while stack:
            (node, depth) = stack.pop()
            if node:
                max_depth = max(max_depth, depth)
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))
                
        return max_depth

    '''
    TC: O(n), 모든 노드 방문
    SC: O(h), 편향 트리 O(h), 균형 시 O(log n), n=h
    '''
    def maxDepthRecurrsion(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)

        return max(left, right) + 1
        