def solution(N, K):
    dp = [1e9 for _ in range(N + 1)]
    dp[0] = 0
    for idx in range(1, N + 1):
        dp[idx] = min(dp[idx], dp[idx - 1] + 1)
        if idx + idx // 2 <= N:
            dp[idx + idx // 2] = min(dp[idx + idx // 2], dp[idx] + 1)

    return 'minigimbob' if dp[-1] <= K else 'water'

N, K = map(int, input().split())
print(solution(N, K))