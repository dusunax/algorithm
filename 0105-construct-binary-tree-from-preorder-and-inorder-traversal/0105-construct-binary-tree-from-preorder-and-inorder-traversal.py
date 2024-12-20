# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # '''
        # - pre: 현재 preorder에서 확인할 인덱스
        # - start, end: inorder에서 사용할 시작/종료 범위
        # '''
        # def setTree(pre, start, end):
        #     # 범위가 잘못되었거나 트리를 더 이상 만들 필요가 없는 경우를 체크
        #     if not (pre < len(preorder) and start <= end): # preorder에서 확인할 인덱스가 범위에서 나감, 투 포인터가 만남
        #         return None
            
        #     val = preorder[pre] # 
        #     root = inorder.index(val)
        #     left = setTree(pre + 1, start, root - 1)
        #     right = setTree(pre + 1 + root - start, root + 1, end)

        #     return TreeNode(preorder[pre], left, right)
        
        # return setTree(0, 0, len(inorder) - 1)
    # def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    #     inorder_index_map = {val: idx for idx, val in enumerate(inorder)}
    #     pre_iter = iter(preorder)
    #     print(inorder_index_map)

    #     def setTree(start, end):
    #         if start > end:
    #             return None
            
    #         root_val = next(pre_iter) # iterate pre_iter for find root
    #         root = inorder_index_map[root_val]

    #         left = setTree(start, root - 1)
    #         right = setTree(root + 1, end)
    #         return TreeNode(root_val, left, right)
        
    #     return setTree(0, len(inorder) - 1)

    '''
    '''
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def setTree(pre_left, pre_right, in_left, in_right):
            if pre_left > pre_right:
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
            