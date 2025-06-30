class Solution:
    # top down
    # n = (n-1) + (n-2) + (n-3)
    def tribonacciDP(self, n: int) -> int:
        memo = {0: 0, 1: 1, 2: 1}

        def dp(n: int) -> int:
            if n in memo:
                return memo[n]
            
            memo[n] = dp(n - 1) + dp(n - 2) + dp(n - 3)
            return memo[n]

        return dp(n)

    # bottom up
    # n+3 = n + (n+1) + (n+2)
    def tribonacci(self, n: int) -> int:
        t0, t1, t2 = 0, 1, 1

        if n == 0: 
            return t0
        if n == 1:
            return t1
        if n == 2:
            return t2

        for _ in range(3, n+1):
            t3 = t0 + t1 + t2
            t0, t1, t2 = t1, t2, t3

        return t2
