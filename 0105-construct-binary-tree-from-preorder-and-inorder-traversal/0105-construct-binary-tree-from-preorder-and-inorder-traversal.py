# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def setTree(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right: # invaild
                return None
            
            root_val = preorder[pre_left]
            root = TreeNode(root_val)

            root_index_in_inorder = inorder_idx_map[root_val] 
            left_tree_size = root_index_in_inorder - in_left

            root.left = setTree(pre_left + 1, pre_left + left_tree_size, in_left, root_index_in_inorder - 1)
            root.right = setTree(pre_left + left_tree_size + 1, pre_right, root_index_in_inorder + 1, in_right)
          
            return root

        inorder_idx_map = {value: idx for idx, value in enumerate(inorder)}

        return setTree(0, len(preorder) - 1, 0, len(inorder) - 1)
        