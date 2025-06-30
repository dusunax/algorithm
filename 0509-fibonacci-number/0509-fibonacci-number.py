class Solution:
    # top down
    def fib(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        def dp(n) -> int:
            if n in memo:
                return memo[n]
            memo[n] = dp(n - 1) + dp(n - 2)

            return memo[n]

        return dp(n)

    # def fib(self, n: int) -> int:
    #     f0, f1 = 0, 1

    #     if n == 0:
    #         return f0
    #     if n == 1:
    #         return f1

    #     for _ in range(2, n + 1):
    #         f2 = f0 + f1
    #         f0, f1 = f1, f2

    #     return f1