# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
# Leetcode 108. Convert Sorted Array to Binary Search Tree

- use recursive function to make the balanced binary search tree.

## Time and Space Complexity

```
TC: O(n)
SC: O(n)
```

### TC is O(n):
- find the middle element (nums[center]) takes constant time = O(1)
- each recursive step, since the size of the array is halved with each recursive step? = O(log n)
- recursive function is called for each element in the array, so the total time complexity is O(n).

### SC is O(n):
- recursion stack space = O(log n)
- space used by the result tree = O(n)
'''
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