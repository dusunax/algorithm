# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # level order traversal: [[], [], []]
        # each nested arrays are a level.
        result = []

         
        # DFS for go through every node.
        def traverseNode (node, level):
            if node is None:
                return

            if len(result) <= level:
                result.append([])   

            if node.val is not None:
                result[level].append(node.val)
            
            if node.left is not None:
                traverseNode(node.left, level + 1)
            if node.right is not None:
                traverseNode(node.right, level + 1)

        traverseNode(root, 0)
        return result