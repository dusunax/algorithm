# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''

기본적인 LCA 문제이다.
- LCA는 BST에서 주어진 두 노드의 Lowest(deepest) Common Ancestor이다.
- 두 노드를 descendants로 가진 노드이며, 두 노드도 포함된다.

재귀 Bottom-up
- p, q가 현재 노드보다 작으면, 왼쪽으로 이동
- p, q가 현재 노드보다 크면, 오른쪽으로 이동
- p, q가 현재 노드에서 양쪽으로 분리되어 나간다면, 현재 노드가 LCA이다.

'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root

    def lowestCommonAncestorTopDown(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left
            elif p.val > root.val and q.val > root.val:
                root = root.right
            else:
                return root 