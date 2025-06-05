# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    '''
    TC: O(n)
    SC: O(1)
    '''
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

'''
# Reverse
- next_node 변수에 curr.next(현재의 다음 노드) 저장
- curr.next에 prev(이전 노드)을 연결
- prev을 curr로 업데이트
- curr를 next_node로 업데이트
- curr가 None일 때까지 반복

next_node 2, curr 1, prev None, 업데이트(curr 2, prev 1)
1 2 3 4 

next_node 3, curr 2, prev 1, 업데이트(curr 3, prev 2)
2 1 3 4 

next_node 4, curr 3, prev 2, 업데이트(curr 4, prev 3)
3 2 1 4 

next_node None, curr 4, prev 3, 업데이트(curr None, prev 4)
4 3 2 1
'''