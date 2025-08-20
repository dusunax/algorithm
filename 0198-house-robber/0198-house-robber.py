'''
## problem
- robbing thoes houses again. 
- houses is in a row.
- no robbing adjacent houses.
- return the maximum amount of money you can rob.

## questions
- do I need a dp table? => yes, and no
  - DP optimization: you don’t store the whole table, just the last two results (prev1, prev2).
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0] 
        if len(nums) == 2:
            return max(nums[0], nums[1])

        prev1 = max(nums[0], nums[1]) 
        prev2 = nums[0]

        for curr in nums[2:]:
            max_money = max(prev1, curr + prev2)
            prev2 = prev1
            prev1 = max_money
            
        return prev1
         