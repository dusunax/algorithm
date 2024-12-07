# get all the cases of the robbery case
# return the maximum amount of money

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            # dp[i - 1]: skip and take the value from the previous house
            # dp[i - 2]: rob the current house, add its value to the maximum money from two houses before
            
        return dp[-1]

        