'''
- circled list
- dp
'''

class Solution:
    # def rob(self, nums: List[int]) -> int:
    #     if len(nums) == 1:
    #         return nums[0]

    #     def robbing(nums):
    #         prev, maxAmount = 0, 0

    #         for num in nums:
    #             prev, maxAmount = maxAmount, max(maxAmount, prev + num)
            
    #         return maxAmount

    #     return max(robbing(nums[1:]), robbing(nums[:-1]))
            
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def robbing(start, end):
            prev, maxAmount = 0, 0

            for i in range(start, end):
                prev, maxAmount = maxAmount, max(maxAmount, prev + nums[i])
            
            return maxAmount

        return max(robbing(0, len(nums) - 1), robbing(1, len(nums)))
