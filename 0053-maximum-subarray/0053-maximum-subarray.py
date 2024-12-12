class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        currentSum = 0 
        maxSum = float('inf') * -1

        for i in range(len(nums)):
            currentSum = max(currentSum + nums[i], nums[i])
            
            if currentSum > maxSum:
                maxSum = currentSum

        return maxSum