class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)
        prefix, suffix = 1, 1

        # prefix
        for i in range(1, len(nums)):
            prefix *= nums[i - 1]
            result[i] = prefix

        # suffix
        for i in range(len(nums) - 2, -1, -1):
            suffix *= nums[i + 1]
            result[i] *= suffix

        return result
        
# answer[i] = product of all elements of nums, except nums[i]

# prefix(0 to i-1) + surfix(i+1 to len-1)

# iterate the array, using nums[i]
# - prefix // 0 to i-1
# - suffix // len-1 to i+1

