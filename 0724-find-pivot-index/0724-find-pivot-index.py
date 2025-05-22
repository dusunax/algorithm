'''
- nums: integer array
- pivot index을 중심으로 left sum == right sum


- left, right 값을 업데이트
'''
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        left_sum = 0
        
        for i, num in enumerate(nums):
            # total - left - num = right
            # left == right => left == total - left - num
            # => 2 * left == total - num
            if 2 * left_sum == total - num:
                return i
            left_sum += num
        
        return -1