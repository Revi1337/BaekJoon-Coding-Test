def solution(N):
    dp = [1e9] * (N + 1)
    dp[0] = dp[1] = 0
    for idx in range(2, N + 1):
        dp[idx] = min(dp[idx], dp[idx - 1] + 1)
        if not idx % 2:
            dp[idx] = min(dp[idx], dp[idx // 2] + 1)
        if not idx % 3:
            dp[idx] = min(dp[idx], dp[idx // 3] + 1)
    return dp[N]

N = int(input())
print(solution(N))