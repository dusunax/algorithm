# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
        pre_iter = iter(preorder)

        def setTree(start, end):
            if start > end:
                return None
            
            root_val = next(pre_iter) # iterate pre_iter for find root
            root = inorder_index_map[root_val]

            left = setTree(start, root - 1)
            right = setTree(root + 1, end)
            return TreeNode(root_val, left, right)
        
        return setTree(0, len(inorder) - 1)

        # def setTree(pre_left, pre_right, in_left, in_right):
        #     if pre_left > pre_right:
        #         return None
            
        #     root_val = preorder[pre_left]
        #     root = TreeNode(root_val)

        #     root_index_in_inorder = inorder_idx_map[root_val] 
        #     left_tree_size = root_index_in_inorder - in_left

        #     root.left = setTree(pre_left + 1, pre_left + left_tree_size, in_left, root_index_in_inorder - 1)
        #     root.right = setTree(pre_left + left_tree_size + 1, pre_right, root_index_in_inorder + 1, in_right)
          
        #     return root

        # inorder_idx_map = {value: idx for idx, value in enumerate(inorder)}

        # return setTree(0, len(preorder) - 1, 0, len(inorder) - 1)
        