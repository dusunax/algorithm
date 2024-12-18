# 
class Solution:
    '''
    1. Bottom-up approach
    '''
    # def climbStairsBU(self, n: int) -> int:
    #     if n == 1 or n == 2:
    #         return n
        
    #     # SC: O(1)
    #     prev2 = 1 # ways to step 0
    #     prev1 = 1 # ways to step 1 

    #     for i in range(3, n + 1): # TC: O(n)
    #         current = prev1 + prev2 # ways to (n-1) + (n-2)
    #         prev2 = prev1
    #         prev1 = current

    #     return prev1

    '''
    2. Top-down approach
    '''
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dp(step: int, memo: int) -> int:
            if step == 1 or step == 2:
                memo[step] = step    
            if step not in memo:
                memo[step] = dp(step - 1, memo) + dp(step - 2, memo)

            return memo[step]

        return dp(n, memo)
