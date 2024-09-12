class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
            
        reversed_str = str(abs(x))[::-1]
        result = int(reversed_str) * (1 if x > 0 else -1)

        if result < -2**31 or result > 2**31 - 1:
            return 0

        return result