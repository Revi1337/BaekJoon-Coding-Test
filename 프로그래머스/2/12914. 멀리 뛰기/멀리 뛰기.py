def solution(N):
    if N == 1:
        return 1
    dp = [0] * (N + 1)
    dp[1], dp[2] = 1, 2
    for seq in range(3, N + 1):
        dp[seq] = (dp[seq - 1] + dp[seq - 2]) % 1234567

    return dp[N]
