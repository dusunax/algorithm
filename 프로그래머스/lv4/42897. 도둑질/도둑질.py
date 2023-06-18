def solution(money):
    dp = [money[0], max(money[0], money[1])]
    dp2 = [0, money[1]]
    n = len(money)

    for i in range(2, n):
        dp.append(max(dp[i-1], dp[i-2] + money[i]))
        dp2.append(max(dp2[i-1], dp2[i-2] + money[i]))

    return max(dp[n - 2], dp2[n - 1])
