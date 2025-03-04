'''
# 236. Lowest Common Ancestor of a Binary Tree

> 관련 문제
> - BST에서 LCA 찾기: 235. Lowest Common Ancestor of a Binary Search Tree

## 재귀 vs 반복문
- 일반 이진 트리는 DFS로 어차피 모든 노드를 순회해야 함
- 반복문은 직접 스택을 짜야하므로, 재귀가 간편하다.

## 재귀 접근
- 트리를 DFS로 순회하며 각 노드에 대해 p와 q의 존재를 확인한다.
- 만약 p 또는 q를 찾으면 그 노드를 반환하고, 찾지 못하면 None을 반환한다.
- 현재 노드가 p 또는 q인 경우, LCA일 수 있으므로 현재 값을 반환한다.
- 두 서브트리에서 모두 값을 찾은 경우, 현재 노드가 LCA이다.
- 하나의 서브트리에서 값을 찾은 경우, 그 값이 LCA이다.
'''
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root == p or root == q: # 현재 노드가 p, q라면 자기 자신이 LCA일 수 있다.
            return root
        
        left = self.lowestCommonAncestor(root.left, p, q) # 왼쪽 서브트리에서 LCA 찾기
        right = self.lowestCommonAncestor(root.right, p, q) # 오른쪽 서브트리에서 LCA 찾기
        
        if left and right: # 만약 왼쪽과 오른쪽에서 각각 p, q를 찾은 경우 현재 노드가 LCA이다.
            return root 
        
        return left if left else right # 만약 한쪽에서만 찾았다면 찾은 쪽이 LCA이다.