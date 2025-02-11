def solution(N):
    dp = [0] * 2001
    dp[1], dp[2] = 1, 2
    for num in range(3, N + 1):
        dp[num] = dp[num - 1] + dp[num - 2]

    return dp[N] % 1234567