# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
'''
# BST에서 k 번째의 값 찾기

- Inorder Traversal: 이진 탐색 트리를 중위 순회하면 트리의 모든 값을 오름 차순으로 방문할 수 있다.
- k번째 가장 작은 값을 구하면 방문을 중단한다.
'''
class Solution:
    # def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    #     result = []

    #     def inorder(node):
    #         if not node:
    #             return
    #         if len(result) > k:
    #             return node

    #         inorder(node.left)
    #         result.append(node.val)
    #         inorder(node.right)
        
    #     inorder(root)

    #     return result[k - 1]

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        result = None

        def inorder(node):
            nonlocal count, result 

            if not node:
                return
            
            inorder(node.left)

            count += 1
            if count == k:
                result = node.val
                return

            inorder(node.right)
        
        inorder(root)

        return result