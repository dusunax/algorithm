class Solution:
    def climbStairs(self, n: int) -> int:
        # 1. Bottom-up
        if n is 1 or n is 2:
            return n
        
        first = 1
        second = 2

        for i in range(3, n + 1):
            curr = first + second
            first = second
            second = curr
        
        return second

