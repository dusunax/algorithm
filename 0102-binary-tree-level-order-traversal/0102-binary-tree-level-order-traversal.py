'''
# Leetcode 102. Binary Tree Level Order Traversal

- travase BT
- return the level order traversal

## approach
- travase with dep parameter => dp(node, dep)
- store the travarse result
'''

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dp(node, dep):
            if node is None:
                return

            if len(result) <= dep:
                result.append([])

            result[dep].append(node.val)
            
            dp(node.left, dep + 1)
            dp(node.right, dep + 1)

        dp(root, 0)

        return result

            

        