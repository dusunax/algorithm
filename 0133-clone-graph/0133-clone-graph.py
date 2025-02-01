"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
            
        visited = {}
        
        def DFS(currNode):
            if currNode.val in visited:
                return visited[currNode.val]

            copiedNode = Node(currNode.val)
            visited[currNode.val] = copiedNode

            for neighbor in currNode.neighbors:
                copiedNode.neighbors.append(DFS(neighbor))

            return copiedNode

        return DFS(node)
