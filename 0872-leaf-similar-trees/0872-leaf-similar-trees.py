# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

'''
# Problem:
- compare the leaf node sequences of 2 binary trees.
- return True if the sequences are the same, otherwise return False.

# Approach1: DFS twice
- get the leaves of the 2 trees by DFS.
- compare if they are same and return the boolean.

# (Test case failed) Approach2: DFS + BFS on the fly
- get the leaves of the root1 tree.
- using BFS, compare the root1 result with leaves of root2
    - return false if they are not match, otherwise continue.
- after compare, return true.
=> ❌ BFS does not guarantee left-to-right leaf order
'''
class Solution:
    '''
    Approach1
    - TC: O(n + m)
        - n for root1's tree's nodes
        - m for root2's tree's nodes.
    - SC: O(h1 + h2 + l)
        - h1 for tree height of root1's tree. 
        - h2 for tree height of root2's tree
        - l for number of leaves.
    '''
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = self.getLeaves(root1)
        leaves2 = self.getLeaves(root2)

        return leaves1 == leaves2
      
    def getLeaves(self, root: Optional[TreeNode]) -> List[int]:
        leaves = []
        self.dfs(root, leaves)
        return leaves
  
    def dfs(self, node: TreeNode, leaves: List[int]) -> List[int]:
        if not node:
            return
        if not node.left and not node.right:
            leaves.append(node.val)
        # no visited check, nothing to do unless it is a leaf node.
        self.dfs(node.left, leaves)
        self.dfs(node.right, leaves)

    # ---------------------------------------
    # This is Approach2, which is not working.
    def leafSimilarNotWorking(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = self.getLeaves(root1)

        queue = deque([root2])
        i = 0

        while queue:
            node = queue.popleft()
            if not node.left and not node.right:
                if i >= len(leaves1) or node.val != leaves1[i]:
                    return False
                i += 1
            else:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
        return i == len(leaves1)