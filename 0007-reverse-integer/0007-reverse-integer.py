class Solution:
    # 1. Convert to string
    # def reverse(self, x: int) -> int:
    #     if x == 0:
    #         return 0
            
    #     reversed_str = str(abs(x))[::-1]
    #     result = int(reversed_str) * (1 if x > 0 else -1)

    #     if result < -2**31 or result > 2**31 - 1:
    #         return 0

    #     return result

    # 2. Use Remainder
    def reverse(self, x: int) -> int:
        num = abs(x)
        res = 0

        while num > 0:
            digit = num % 10
            num //= 10

            if res > ((2 ** 31 - 1) // 10) or ((res == 2 ** 31 - 1) // 10 and digit > 7):
                return 0

            res = res * 10 + digit

        return res * (1 if x > 0 else -1)
    