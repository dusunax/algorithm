'''
- find the single integer among the duplicates
- bitwise XOR op => will convert 0 to 1, 1 to 0
- if we XOR the same number twice? => it cancels out, returns to before
- so, all duplicates cancel each other out => XORing all integers, only the single number remains
'''
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for num in nums:
            result ^= num
        return result