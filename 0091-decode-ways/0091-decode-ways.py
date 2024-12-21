'''
# dp
헬퍼함수: 1~26인 경우 True
n: 문자열 s의 길이
dp: 결과를 저장할 배열, n+1
BaseCase: dp[0] = 1, dp[1] = 1
for loop 2 to n:
    one = s의 i-1 위치의 1글자 (현재 글자)
    two = s의 i-2부터 i까지 자른 2글자 (현재 글자 포함 이전 글자)
    if one is decodable => dp[i] += dp[i - 1] i길이일 때, dp의 -1 경우의 만큼수 추가 (현재 글자를 한 글자로 해석)
    if two is decodable => dp[i] += dp[i - 2] i길이일 때, dp의 -2 경우의 수 만큼 추가 (현재 글자를 두 글자로 해석)
dp[n]: 최종 디코드 가능한 경우의 수 결과
'''
class Solution:
    def isDecodable(self, int: int):
        return 1 <= int <= 26

    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)
        dp = (n + 1) * [0]
        dp[0] = 1
        dp[1] = 1

        for i in range(2, n + 1):
            one = int(s[i - 1])
            two = int(s[i - 2:i])

            if self.isDecodable(one):
                dp[i] += dp[i - 1]
            if self.isDecodable(two):
                dp[i] += dp[i - 2]

        return dp[n]
