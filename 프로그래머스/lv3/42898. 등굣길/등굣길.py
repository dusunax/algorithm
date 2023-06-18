def solution(m, n, puddles):
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    dp[1][1] = 1  # 집 위치: 1
    for x, y in puddles:
        dp[x][y] = -1 # 물에 잠긴 지역: -1

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if i == 1 and j == 1:
                continue
            if dp[i][j] == -1:
                continue

            # 왼쪽에서 왔을 때
            if j > 1 and dp[i][j - 1] != -1:
                dp[i][j] += dp[i][j - 1] % 1000000007

            # 오른쪽에서 왔을 때
            if i > 1 and dp[i - 1][j] != -1:
                dp[i][j] += dp[i - 1][j] % 1000000007

            dp[i][j] %= 1000000007

    return dp[m][n]
