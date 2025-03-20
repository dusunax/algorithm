'''
'''

class Solution:
    def longestPalindromeDP(self, s: str) -> str:
        n = len(s)
        if n == 1:
            return s
        
        start, length = 0, 1
        dp = [[False] * n for _ in range(n)]

        # length 1, diagonal elements in 2d array
        for i in range(n):
            dp[i][i] = True

        # length 2, are two elements same
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

    def longestPalindrome(self, s: str) -> str:
        # 문자열을 변환하여 짝수 길이의 팰린드롬을 처리
        transformed = '#' + '#'.join(s) + '#'
        n = len(transformed)
        p = [0] * n  # 각 중심에서의 팰린드롬 반지름을 저장
        c = 0  # 현재 팰린드롬의 중심
        r = 0  # 현재 팰린드롬의 오른쪽 끝
        max_len = 0  # 가장 긴 팰린드롬의 길이
        center = 0  # 가장 긴 팰린드롬의 중심

        for i in range(n):
            # 현재 위치 i의 미러 인덱스 (대칭되는 인덱스)
            mirror = 2 * c - i

            if i < r:
                # 이미 계산된 팰린드롬 반지름을 사용하여 확장을 최소화
                p[i] = min(r - i, p[mirror])

            # 현재 중심에서 팰린드롬을 확장
            while i + p[i] + 1 < n and i - p[i] - 1 >= 0 and transformed[i + p[i] + 1] == transformed[i - p[i] - 1]:
                p[i] += 1

            # 만약 팰린드롬이 오른쪽 끝을 넘어서면, 새로운 중심과 오른쪽 끝을 설정
            if i + p[i] > r:
                c = i
                r = i + p[i]

            # 가장 긴 팰린드롬 업데이트
            if p[i] > max_len:
                max_len = p[i]
                center = i

        # 변환된 문자열에서 가장 긴 팰린드롬을 원래 문자열에서 추출
        start = (center - max_len) // 2
        return s[start:start + max_len]

'''
## Leetcode Hints
- How can we reuse a previously computed palindrome to compute a larger palindrome?
  - use dp table that stores isPalindrome computation.
- If “aba” is a palindrome, is “xabax” a palindrome? Similarly is “xabay” a palindrome?
  - if it is palindrome, we only need to check the right outside chars, that wrapping our palindrome.
- Palindromic checks can be O(1) by reusing prev computation.
  - dp!

## 풀이
- s[i:j]의 팰린드롬 여부를 저장하기 위해서는 2차원 배열을 사용하는 것이 간편하다.
- 길이가 1인 경우, 팰린드롬
- 길이가 2인 경우, 두 문자가 같다면 팰린드롬
- 3 이상은 dp 테이블을 활용하여 확인
- 길이가 5인 문자열을 다음과 같이 탐색
```
len: 3, i: 0, j: 2
len: 3, i: 1, j: 3
len: 3, i: 2, j: 4
len: 4, i: 0, j: 3
len: 4, i: 1, j: 4
len: 5, i: 0, j: 4
```

## 탐구
- can we use sliding window for optimize?
슬라이딩 윈도우는 연속적인 구간을 유지하며 최적해를 찾을 때 유용하지만, 팰린드롬은 중앙 확장과 이전 계산 재사용이 핵심.

- can we solve this by counting char?
문자 개수를 세면 "어떤 문자가 몇 번 나왔는지"만 알 수 있지만, 팰린드롬 여부는 문자 순서가 중요하다.

- 그렇다면 개선할 수 있는 방법은? => Manacher's Algorithm 
팰린드롬의 대칭성을 활용해 중앙을 기준으로 확장하는 Manacher's Algorithm을 적용할 수 있다.
모든 문자 사이에 #을 넣어 짝수, 홀수를 동일하게 다루는 기법인데 구현이 다소 복잡하다.
'''