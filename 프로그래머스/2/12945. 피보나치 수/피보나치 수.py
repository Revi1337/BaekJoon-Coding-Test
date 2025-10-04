def solution(n):
    dp = [0] * (n + 1)
    dp[1] = 1
    for seq in range(2, n + 1):
        dp[seq] = dp[seq - 1] + dp[seq - 2]

    return dp[n] % 1234567