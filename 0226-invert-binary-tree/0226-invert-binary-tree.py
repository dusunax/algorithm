# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTreeRecursive(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        root.left, root.right = root.right, root.left

        self.invertTree(root.left)
        self.invertTree(root.right)

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stack = [root]

        while stack:
            node = stack.pop()
            if not node:
                continue
            
            node.left, node.right = node.right, node.left
            stack.append(node.left)
            stack.append(node.right)

        return root

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dq = deque([root])

        while dq:
            node = dq.popleft()
            if not node:
                continue
            
            node.left, node.right = node.right, node.left
            dq.append(node.left)
            dq.append(node.right)

        return root
