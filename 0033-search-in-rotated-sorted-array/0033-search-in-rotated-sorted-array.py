class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # is_left_sorted
                if nums[left] <= target < nums[mid]: # is_target_left
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]: # is_target_right
                    left = mid + 1
                else:
                    right = mid - 1

        return -1