def solution(triangle):
    n = len(triangle)
    dp = triangle.copy()  # dp 테이블 준비
    
    for i in range(1, n):  # 각 레벨(시작 노드를 제외)
        for j in range(i + 1):
            # 1 레벨: 0~1 요소
            # 2 레벨: 0~2 요소
            # ...
            if j == 0:  # 맨 왼쪽 노드
                dp[i][j] += dp[i - 1][0]  # 현재 노드 += 부모 노드(맨 왼쪽)
            elif j == i:  # 맨 우측 노드
                dp[i][j] += dp[i - 1][j - 1]  # 현재 노드 += 부모 노드(맨 오른쪽)
            else:  # 중간 노드: 부모 노드 2개
                dp[i][j] += max(dp[i - 1][j - 1], dp[i - 1][j])
    
    return max(dp[n - 1])  # 마지막 레벨의 최대값
