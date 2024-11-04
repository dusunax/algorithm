class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. Bottom-up
        if n == 1 or n == 2:
            return n
        
        first = 1
        second = 2

        for i in range(3, n + 1):
            curr = first + second
            first = second
            second = curr
        
        return second

        # 2. Top-bottom
        # memo = {}
        # def dp (self, step, memo) -> int:
        #     if step == 1 or step == 2:
        #         return step
        #     if step in memo:
        #         return memo[step]
        #     memo[step] = dp(self, step -1, memo) + dp(self, step - 2, memo)
        #     return memo[step]
        
        # return dp(self, n, memo)

# \U0001f4cc Python!
# use `if step in memo``, not `if memo[step]``

# Unnecessary self
# - https://www.geeksforgeeks.org/self-in-python-class/
# - you don’t need to include self in each call => it’s defined within the scope of the method climbStairs\U0001f914

# use `==`` for comparison, not `is`