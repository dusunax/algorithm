# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def makeBalancedBSTWithArray(nums) -> Optional[TreeNode]:
            if not nums:
                return None
            
            center = int(len(nums) / 2)
            middleNode = TreeNode(nums[center])
            
            middleNode.left = makeBalancedBSTWithArray(nums[:center])
            middleNode.right = makeBalancedBSTWithArray(nums[center + 1:])

            return middleNode

        return makeBalancedBSTWithArray(nums)
        
        

