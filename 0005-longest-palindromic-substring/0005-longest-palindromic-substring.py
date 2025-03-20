'''
## Hints
- How can we reuse a previously computed palindrome to compute a larger palindrome?
use dp that stores a possible longest palindromes.

- If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
if it is palindrome, we only need to check the right outside chars, that wrapping our palindrome.

- Palindromic checks can be O(1) by reusing prev computation.

## Approach
- sliding window: pointers for moving window.
- return the longest string.

\U0001f914.
- can we use sliding window for optimize? (need to?)
- can we solve this by counting char?

이렇게 탐색
len: 3, i: 0, j: 2
len: 3, i: 1, j: 3
len: 3, i: 2, j: 4
len: 4, i: 0, j: 3
len: 4, i: 1, j: 4
len: 5, i: 0, j: 4

s[i:j]의 팰린드롬 여부를 저장하기 위해서는 2차원 배열을 사용하는 것이 적합하다.

'''

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        
        start, length = 0, 1
        dp = [[False] * n for _ in range(n)]

        # length 1, 2d diagonal elements
        for i in range(n):
            dp[i][i] = True

        # length 2
        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                start, length = i, 2

        # length 3+
        for word_length in range(3, n + 1):
            for i in range(n - word_length + 1):
                j = i + word_length - 1

                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    start, length = i, word_length
                
        return s[start:start + length]
