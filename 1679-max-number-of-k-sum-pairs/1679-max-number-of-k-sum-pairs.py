'''
pick two numbers for the array, that sum == k
=> remove two numbers

return the maximum number of ops can perform

- are they sorted? => no.
- do we need to sort first? => yes
- python .sorted() is in place? => yes
- do we need to actually delete the num from array? => no

when we check the results of `nums[left] + numse[right]`. There is 3 cases
1. result is equal to k 2. result is smaller than k 3. result is bigger than k
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        count = 0
        left = 0
        right = len(nums) - 1
        nums.sort()

        while left < right:
            current_sum = nums[left] + nums[right] 
            
            if current_sum == k:
                left += 1
                right -= 1
                count += 1
            elif current_sum < k:
                left += 1
            else:
                right -= 1

        return count