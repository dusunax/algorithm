class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        while len(nums):
            current = nums.pop()
            if current not in nums:
                return current
            nums.remove(current)