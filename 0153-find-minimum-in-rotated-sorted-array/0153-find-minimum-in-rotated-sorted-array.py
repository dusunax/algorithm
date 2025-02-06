class Solution:
    def findMinON(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        return min(nums)
        
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]

        